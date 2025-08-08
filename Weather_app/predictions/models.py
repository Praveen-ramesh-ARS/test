from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.db import models

class PredictionLog(models.Model):
    city = models.CharField(max_length=100)
    temperature = models.FloatField()
    humidity = models.FloatField()
    wind_speed = models.FloatField()
    pressure = models.FloatField()
    prediction = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.city} - {self.temperature}"



    