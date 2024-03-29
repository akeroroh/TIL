from django.db import models

# Create your models here.
class Travels(models.Model):
    location = models.CharField(max_length=50)
    plan = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()