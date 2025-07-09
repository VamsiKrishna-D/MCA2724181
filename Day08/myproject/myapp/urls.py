from django.urls import path
from . import views
urlpatterns = [
   path('insert_employee/',views.insert_employee,name='insert_employee'),
    # other paths as needed
]
