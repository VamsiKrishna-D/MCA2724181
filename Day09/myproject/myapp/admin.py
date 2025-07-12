from django.contrib import admin

# Register your models here.
from .models import EmployeeModel
admin.site.register(EmployeeModel)
