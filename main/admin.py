from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from main.models import User, Role, Department, MealCategory, Check, MealID, Meal, ServicePercentage, Status, Table, Order

admin.site.register(User)
admin.site.register(Role)
admin.site.register(Department)
admin.site.register(MealCategory)
admin.site.register(ServicePercentage)
admin.site.register(Status)
admin.site.register(Table)
admin.site.register(Order)
admin.site.register(Meal)
admin.site.register(MealID)
admin.site.register(Check)


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ('email', 'is_staff', 'is_active',)
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)