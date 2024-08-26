import uuid
from django.db import models

# Create your models here.

class Forecast(models.Model):
    location = models.CharField(max_length=200)
    temp_in_f = models.CharField(max_length=2)
    temp_in_c = models.CharField(max_length=2)
    uuid = models.UUIDField(unique=True, primary_key=True, editable=False, default=uuid.uuid4)

