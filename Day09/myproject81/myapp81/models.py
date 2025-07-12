from django.db import models

# Create your models here.
class StudentModel(models.Model):  
    name = models.CharField(max_length=30)  
    course = models.CharField(max_length=30)
    ht_no= models.CharField(max_length=10, unique=True)
    mobile = models.CharField(max_length=10, unique=True)  
    pov=models.CharField(max_length=9)
  
    def __str__(self):  
        return (self.name+' '+ self.course)
class FacultyModel(models.Model):  
    name = models.CharField(max_length=30)  
    subject = models.CharField(max_length=30)  
    mobile = models.CharField(max_length=10, unique=True)  
    email = models.EmailField()  
  
    def __str__(self):  
        return (self.name)
class EmployeeModel(models.Model):  
    first_name = models.CharField(max_length=30)  
    last_name = models.CharField(max_length=30)  
    mobile = models.CharField(max_length=10, unique=True)  
    email = models.EmailField()  
  
    def __str__(self):  
        return (self.first_name+' '+ self.last_name)