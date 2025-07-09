from django.urls import path
from . import views

urlpatterns = [
    path('list_students/', views.list_students, name='list_students'),
    path('add/', views.add_student, name='add_student'),
    path('edit/<int:rollno>/', views.edit_student, name='edit_student'),
    path('delete/<int:rollno>/', views.delete_student, name='delete_student'),
    path('green/',views.green,name='green'),
]
