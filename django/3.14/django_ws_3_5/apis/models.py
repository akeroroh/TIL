from django.db import models
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

def validate_url_length(value):
    validator = URLValidator()
    if len(value) < 15 or len(value) > 60:
        raise ValidationError("Invalid URL")

class APIInfo(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    api_url = models.URLField(validators=[validate_url_length])
    documentation_url = models.URLField()
    auth_required = models.BooleanField()
    additional_info = models.JSONField(default=None, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
