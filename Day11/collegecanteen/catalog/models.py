from django.db import models

# Create your models here.
class FoodItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='food/', blank=True, null=True)

    def __str__(self):
        return self.name
