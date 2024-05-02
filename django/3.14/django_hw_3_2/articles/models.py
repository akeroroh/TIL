from django.db import models

# Create your models here.
class article(models.Model):
    title = models.TextField(max_length=15)
    content = models.TextField()