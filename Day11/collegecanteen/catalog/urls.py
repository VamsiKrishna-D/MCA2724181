from django.urls import path
from . import views

urlpatterns = [
    path('', views.food_list, name='food_list'),
    path('food/<int:pk>/', views.food_detail, name='food_detail'),
    path('food/add/', views.food_create, name='food_create'),
    path('food/<int:pk>/edit/', views.food_update, name='food_update'),
    path('food/<int:pk>/delete/', views.food_delete, name='food_delete'),
]
