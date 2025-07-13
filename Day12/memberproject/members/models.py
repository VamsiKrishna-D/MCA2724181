from django.db import models

class Member(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    joined_date = models.DateField()

    def _str_(self):
        return f"{self.firstname} {self.lastname}"
