from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class ParkingTime(models.Model):
    time_time = models.IntegerField(null=True)
    duration = models.IntegerField(null=True)
    user_id = models.IntegerField(null=True)
    parking_place_id = models.IntegerField(null=True)


class ParkingPlace(models.Model):
    description = models.CharField(default='Just parking place', max_length=50)
