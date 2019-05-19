from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from main.models import (
    Table, Role, Status, Meal,
    Order, User, UserManager, MealID,
    MealCategory, ServicePercentage,
    Department, Check
)
from main.serializers import *


class TableView(APIView):

    def get(self, request, pk):
        table = Table.objects.get(id=pk)
        serializer = TableSerializer(table)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        Table.objects.filter(id=pk).delate()
        return Response(status=status.HTTP_201_CREATED)

    # def update(self, request, pk):


class TableViewList(APIView):

    def get(self, request):
        tables = Table.objects.all()
        serializer = TableSerializer(tables, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = TableSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_400_BAD_REQUEST)


class RoleView(APIView):

    def get(self, request, pk):
        role = Role.objects.get(id=pk)
        serializer = RoleSerializer(role)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        Role.objects.filter(id=pk).delate()
        return Response(status=status.HTTP_201_CREATED)

    # def update(self, request, pk):


class RoleViewList(APIView):

    def get(self, request):
        roles = Role.objects.all()
        serializer = RoleSerializer(roles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = RoleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_400_BAD_REQUEST)


class DepartmentView(APIView):

    def get(self, request, pk):
        department = Department.objects.get(id=pk)
        serializer = DepartmentSerializer(department)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        Department.objects.filter(id=pk).delate()
        return Response(status=status.HTTP_201_CREATED)

    # def update(self, request, pk):


class DepartmentViewList(APIView):

    def get(self, request):
        departments = Department.objects.all()
        serializer = DepartmentSerializer(departments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = DepartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_400_BAD_REQUEST)


class MealCategoryView(APIView):

    def get(self, request, pk):
        mealcategory = MealCategory.objects.get(id=pk)
        serializer = MealCategorySerializer(mealcategory)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        MealCategory.objects.filter(id=pk).delate()
        return Response(status=status.HTTP_201_CREATED)

    # def update(self, request, pk):


class MealCategoryViewList(APIView):

    def get(self, request):
        mealcategories = MealCategory.objects.all()
        serializer = MealCategorySerializer(mealcategories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = MealCategorySerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CategoriesByDepartmentViewList(APIView):

    def get(self, request, pk):
        mealcategories = Department.objects.get(id=pk).mealcategory_set
        serializer = MealCategorySerializer(mealcategories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class StatusView(APIView):

    def get(self, request, pk):
        status = Status.objects.get(id=pk)
        serializer = StatusSerializer(status)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        Status.objects.filter(id=pk).delate()
        return Response(status=status.HTTP_201_CREATED)


class StatusViewList(APIView):

    def get(self, request):
        statuses = Status.objects.all()
        serializer = StatusSerializer(statuses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = StatusSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_400_BAD_REQUEST)


class ServicePercentageView(APIView):

    def get(self, request):
        percentage = ServicePercentage.objects.get(id=1)

        serializer = ServicePercentageSerializer(percentage)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request):
        percentage = ServicePercentage.objects.get(pk=1)
        serializer = ServicePercentageSerializer(percentage, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class MealsView(APIView):

    def get(self, request, pk):
        meal = Meal.objects.get(pk=pk)
        serializer = MealSerializer(meal)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        Meal.objects.get(pk=pk).delate()
        return Response(status=status.HTTP_201_CREATED)

    def put(self, request, pk):
        meal = Meal.objects.get(pk=pk)
        serializer = MealSerializer(meal, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class MealsViewList(APIView):

    def get(self, request):
        meals = Meal.objects.all()
        serializer = MealSerializer(meals, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = MealSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_400_BAD_REQUEST)


class MealsByCategory(APIView):

    def get(self, request, pk):
        meals = MealCategory.objects.get(id=pk).meal_set
        serializer = MealSerializer(meals, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class OrderView(APIView):

    def get(self, request, pk):
        order = Order.objects.get(pk=pk)
        serializer = OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        Order.objects.get(pk=pk).delete()
        return Response(status=status.HTTP_201_CREATED)


class OrderViewList(APIView):

    def get(self, request):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = OrderSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.error_messages)
        print(serializer.errors)
        return Response(status=status.HTTP_400_BAD_REQUEST)

'''
{
    "tableid": 2,
    "meals" : [
        {
            "id": 1,
            "name": "plov", 
            "count": 3
        },
        {
            "id": 2,
            "name": "lagman",
            "count": 1
        }
    ]
}
'''