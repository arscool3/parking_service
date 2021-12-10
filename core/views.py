from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import *
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from .models import ParkingPlace, ParkingTime



class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()

    def get_serializer_class(self):
        pk = self.kwargs['pk']
        if pk == 1:
            return UserCreateSerializer
        else:
            return SuperUserCreateSerializer


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer


class GetParkingPlace(generics.ListAPIView):
    queryset = ParkingPlace.objects.all()
    serializer_class = ParkingPlaceSerializer
    permission_classes = (IsAuthenticated,)


class GetParkingTime(generics.ListAPIView):
    def get_queryset(self):
        id = self.kwargs['pk']
        return ParkingTime.objects.filter(parking_place_id=id)

    serializer_class = ParkingTimeSerializer
    permission_classes = (IsAuthenticated,)


class SetParkingTime(generics.CreateAPIView):
    queryset = ParkingTime.objects.all()
    serializer_class = ParkingTimeCreateSerializer

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user.id)

    permission_classes = (IsAuthenticated,)


class GetYourTime(generics.ListAPIView):
    serializer_class = ParkingTimeSerializer

    def get_queryset(self):
        return ParkingTime.objects.filter(user_id=self.request.user.id)

    permission_classes = (IsAuthenticated,)


class DeleteTime(generics.DestroyAPIView):
    serializer_class = ParkingTimeSerializer

    def get_queryset(self):
        return ParkingTime.objects.filter(id=self.kwargs['pk'])

    def get_permissions(self):
        parking_time = None
        for parking_time_index in ParkingTime.objects.filter(id=self.kwargs['pk']):
            parking_time = parking_time_index
        if self.request.user.id == parking_time.user_id:
            self.permission_classes = (IsAuthenticated,)
        else:
            self.permission_classes = (IsAdminUser,)
        return super(self.__class__, self).get_permissions()


class AddPlace(generics.CreateAPIView):
    serializer_class = ParkingPlaceSerializer
    queryset = ParkingPlace.objects.all()
    permission_classes = (IsAdminUser,)


class EditPlace(generics.UpdateAPIView):
    serializer_class = ParkingPlaceSerializer

    def get_queryset(self):
        return ParkingPlace.objects.filter(id=self.kwargs['pk'])

    permission_classes = (IsAdminUser,)


class DeletePlace(generics.DestroyAPIView):
    serializer_class = ParkingPlaceSerializer

    def get_queryset(self):
        return ParkingPlace.objects.filter(id=self.kwargs['pk'])

    permission_classes = (IsAdminUser,)
