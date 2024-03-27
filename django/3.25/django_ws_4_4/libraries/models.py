from django.db import models

# Create your models here.
class Book(models.Model):
    isbn = models.TextField()
    author = models.TextField()
    title = models.TextField()
    Category_name = models.TextField()
    Category_id = models.IntegerField()
    price = models.IntegerField()
    Fixed_price = models.BooleanField()
    pub_date = models.DateField()