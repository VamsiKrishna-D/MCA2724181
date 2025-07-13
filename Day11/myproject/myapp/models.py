from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_number = models.IntegerField(unique=True)
    course = models.CharField(max_length=100)
    enrollment_date = models.DateField()

    def __str__(self):
        return self.name
