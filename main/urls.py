from django.urls import path

from main.views import *

'''
(
    TableViewList, TableView,
    RoleViewList, RoleView,
    DepartmentViewList, DepartmentView,
    MealCategoryView, MealCategoryViewList, CategoriesByDepartmentViewList,
    StatusView, StatusViewList,
    ServicePercentageView,
)
'''

app_name = 'main'

urlpatterns = [
    path('tables/', TableViewList.as_view(), name='tables'),
    path('tables/<int:pk>/', TableView.as_view(), name='table'),

    path('roles/', RoleViewList.as_view(), name='roles'),
    path('roles/<int:pk>/', RoleView.as_view(), name='role'),

    path('departments/', DepartmentViewList.as_view(), name='roles'),
    path('departments/<int:pk>/', DepartmentView.as_view(), name='role'),

    path('mealcategory/', MealCategoryViewList.as_view(), name='mealcategories'),
    path('mealcategory/<int:pk>/',MealCategoryView.as_view(), name='mealcategory'),
    path('categoriesbydepartment/<int:pk>', CategoriesByDepartmentViewList.as_view(), name='categoriesbydepartment'),

    path('statuses/', StatusViewList.as_view(), name='statuses'),
    path('statuses/<int:pk>/', StatusView.as_view(), name='status'),

    path('servicepercentage/', ServicePercentageView.as_view(), name='percentage'),

    path('meals/', MealsViewList.as_view(), name='meals'),
    path('meals/<int:pk>/', MealsView.as_view(), name='meal'),
    path('mealsbycategory/<int:pk>/', MealsByCategory.as_view(), name='mealsbycategory'),

    path('orders/', OrderViewList.as_view(), name='orders'),
]
