from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.name

class Customer(models.Model):
    product = models.ManyToManyField('Product')
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    def __str__(self):
        return self.name
