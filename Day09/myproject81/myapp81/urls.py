from django.urls import path
from . import views
urlpatterns = [
   path('',views.display_home,name='display_home'),
   path('insert_employee/',views.insert_employee, name='insert_employee'),
   path('view_employee/', views.view_employee,  name = 'view_employee'),
   path('insert_faculty/',views.insert_faculty, name='insert_faculty'),
   path('view_faculty/', views.view_faculty,  name = 'view_faculty'),
   path('insert_student/',views.insert_student, name='insert_student'),
   path('view_student/', views.view_student,  name = 'view_student'),
   path('view_faculty_delete/', views.view_faculty_delete,  name = 'view_faculty_delete'),
   path('delete_faculty/<int:pk>', views.delete_faculty,
           name = 'delete_faculty'),
   ]
