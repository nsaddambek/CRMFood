from rest_framework import serializers

from main.models import (
    Table, Department, ServicePercentage,
    MealCategory, Meal, User, UserManager,
    Status, Role, Order, MealID, Check
)


class TableSerializer(serializers.ModelSerializer):

    class Meta:
        model = Table
        fields = '__all__'


class RoleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Role
        fields = '__all__'


class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Department
        fields = '__all__'


class MealCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = MealCategory
        fields = '__all__'


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'


class ServicePercentageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ServicePercentage
        fields = ['price']


class MealSerializer(serializers.ModelSerializer):

    class Meta:
        model = Meal
        fields = '__all__'

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.categoryid = validated_data.get('categoryid', instance.categoryid)
        instance.price = validated_data.get('price', instance.price)
        instance.description = validated_data.get('description', instance.description)

        instance.save()

        return instance


class MealIDSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(
        source='meal.id'
    )

    name = serializers.CharField(
        source='meal.name'
    )

    class Meta:
        model = MealID
        fields = ['id', 'name', 'count']


class OrderSerializer(serializers.ModelSerializer):
    waiterid = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    tableid = serializers.IntegerField(
        source='table.id'
    )

    tablename = serializers.CharField(
        source='table.name',
        read_only=True
    )

    mealsid = MealIDSerializer(
        source='meals',
        many=True,
    )

    class Meta:
        model = Order
        fields = ['id', 'waiterid', 'tableid', 'tablename', 'isitopen', 'date', 'mealsid']

    def create(self, validated_data):
        meal_data = validated_data.pop('mealsid')

        order = Order.objects.create(isitopen=True, table=validated_data['table'])

        for meal in meal_data:
            MealID.objects.create(
                order=order,
                meal=meal['id'],
                count=meal['count']
            ).save()

        order.save()

        return order
