from django.contrib import admin
from .models import ParkingPlace, ParkingTime


admin.site.register(ParkingPlace)
admin.site.register(ParkingTime)