from django.urls import path
from .views import (
    StudentCreateView,
    StudentListView,
    StudentUpdateView,
    StudentDeleteView,
)

urlpatterns = [
    path('', StudentListView.as_view(), name='student_list'),
    path('create/', StudentCreateView.as_view(), name='student_create'),
    path('update/<int:pk>/', StudentUpdateView.as_view(), name='student_update'),
    path('delete/<int:pk>/', StudentDeleteView.as_view(), name='student_delete'),
]
