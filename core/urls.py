from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('register/<int:pk>', RegisterView.as_view()),
    path('login/', MyObtainTokenPairView.as_view()),
    path('places/', GetParkingPlace.as_view()),
    path('places/<int:pk>', GetParkingTime.as_view()),
    path('add/time/', SetParkingTime.as_view()),
    path('get/time/', GetYourTime.as_view()),
    path('delete/time/<int:pk>', DeleteTime.as_view()),
    path('add/place/', AddPlace.as_view()),
    path('edit/place/<int:pk>', EditPlace.as_view()),
    path('delete/place/<int:pk>', DeletePlace.as_view())

]
