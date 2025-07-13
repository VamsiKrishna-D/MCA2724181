from django.db import models

# Create your models here.
class Member(models.Model):
  id=models.CharField(max_length=255 ,primarykey=True)
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  phone = models.IntegerField(null=True) 
  joined_date = models.DateField(null=True)
  def __str__(self):
    return self.id