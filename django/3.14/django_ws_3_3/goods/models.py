from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_published = models.BooleanField()
    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)