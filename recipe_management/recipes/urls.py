# recipes/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_recipes, name='list_recipes'),
    path('add/', views.add_recipe, name='add_recipe'),
    path('edit/<int:pk>/', views.edit_recipe, name='edit_recipe'),
    path('delete/<int:pk>/', views.delete_recipe, name='delete_recipe'),
]