from django.db import models

# Create your models here.
class APOinfo(models.Model):
    name = models.TextField(max_length=200)
    description = models.TextField()
    api_url = models.URLField()
    documentation_url = models.URLField()
    auth_required = models.BooleanField()
    additionl_info = models.JSONField()
    created_at = models.DateField(auto_now_add=True)
