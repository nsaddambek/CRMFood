from django.contrib import admin

from main.models import User, Role, Departament, MealCategory, Check, MealID, Meal, ServicePercentage, Status, Table, Order

admin.site.register(User)
admin.site.register(Role)
admin.site.register(Departament)
admin.site.register(MealCategory)
admin.site.register(ServicePercentage)
admin.site.register(Status)
admin.site.register(Table)
admin.site.register(Order)
admin.site.register(Meal)
admin.site.register(MealID)
admin.site.register(Check)
