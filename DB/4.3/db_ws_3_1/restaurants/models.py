from django.db import models

# Create your models here.
class Restaurant(models.Model):
    category = models.ForeignKey('category', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    address = models.CharField(max_length=200)
    opening_time = models.TimeField()
    closing_time = models.TimeField()

class Menu(models.Model):
    restaurant = models.ForeignKey("restaurant", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    is_vegan = models.BooleanField()

class Category(models.Model):
    name = models.CharField(max_length=20)