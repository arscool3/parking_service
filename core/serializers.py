from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=True)
    username = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ('username', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(username=validated_data['username'], password=validated_data['password'])
        return user


class SuperUserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=True)
    username = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ('username', 'password')

    def create(self, validated_data):
        user = User.objects.create_superuser(username=validated_data['username'], password=validated_data['password'])
        return user


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)
        token['username'] = user.username
        return token


class ParkingPlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkingPlace
        fields = '__all__'


class ParkingTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkingTime
        fields = '__all__'


class ParkingTimeCreateSerializer(serializers.ModelSerializer):
    time = serializers.IntegerField(required=True)
    duration = serializers.IntegerField(required=True)
    parking_place_id = serializers.IntegerField(required=True)


    class Meta:
        model = ParkingTime
        fields = ('time_time', 'duration', 'parking_place_id')

    def create(self, validated_data):
        for parking_time in ParkingTime.objects.filter(parking_place_id=validated_data['parking_place_id']):

            time = parking_time.time
            duration = parking_time.duration
            if time <= validated_data['time_time'] < time + duration or validated_data['time_time'] < time and validated_data[
                'time_time'] + validated_data['duration'] > time:
                raise ValueError('Cannot set time')
        return ParkingTime.objects.create(**validated_data)


class ParkingTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkingTime
        fields = '__all__'
