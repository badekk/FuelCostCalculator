from django.db import models

# Create your models here.


class Car(models.Model):
    car_make = models.CharField(max_length=40, blank=False)
    car_model = models.CharField(max_length=40, blank=False)
    car_consumption = models.DecimalField(max_digits=4, decimal_places=2, blank=False)

