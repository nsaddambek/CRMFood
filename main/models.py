from django.utils.translation import gettext_lazy as _
from .managers import UserManager
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin
)


class Role(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class User(AbstractBaseUser, PermissionsMixin):
    role = models.ForeignKey(Role, null=True, on_delete=models.SET_NULL)
    name = models.CharField(db_index=True, max_length=255, null=True)
    surname = models.CharField(db_index=True, max_length=255, null=True)
    login = models.CharField(max_length=255, unique=True)
    email = models.EmailField(_('email address'), unique=True)
    phone = models.CharField(max_length=100, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'login'
    REQUIRED_FIELDS = ['email', ]

    objects = UserManager()

    def __str__(self):
        return self.login


class Department(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class MealCategory(models.Model):
    name = models.CharField(max_length=50)
    departmentid = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class ServicePercentage(models.Model):
    price = models.IntegerField()

    def __str__(self):
        return str(self.price)


class Status(models.Model):

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Table(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Meal(models.Model):
    name = models.CharField(max_length=50)
    categoryid = models.ForeignKey(MealCategory, on_delete=models.CASCADE)
    price = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name


class Order(models.Model):
    waiterid = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    table = models.ForeignKey(Table, on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(auto_now_add=True)
    isitopen = models.BooleanField(default=True)
    meals = models.ManyToManyField(Meal, through='MealID')

    def get_cost(self):
        return sum(item.get_price() for item in self.mealid_set.all())


class MealID(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    count = models.IntegerField()

    def get_price(self):
        return self.meal.price * self.count


class Check(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    servicefee = models.ForeignKey(ServicePercentage, on_delete=None)

    def get_total_cost(self):
        return self.order.get_cost() + self.servicefee.price
