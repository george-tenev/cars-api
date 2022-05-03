from rest_framework import generics, permissions

from cars_app.cars_api.filters import UserCarListFilterSet, CarBrandListFilterSet, CarModelListFilterSet
from cars_app.cars_api.models import UserCar, CarBrand, CarModel
from cars_app.cars_api.serializers import UserCarSerializer, CarBrandSerializer, CarModelSerializer


class UserCarsListCreate(generics.ListCreateAPIView):
    queryset = UserCar.objects.all()
    serializer_class = UserCarSerializer
    filterset_class = UserCarListFilterSet
    permission_classes = (
        permissions.IsAuthenticated,
    )


class UserCarsRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserCar.objects.all()
    serializer_class = UserCarSerializer
    permission_classes = (
        permissions.IsAuthenticated,
    )


class CarBrandListCreate(generics.ListCreateAPIView):
    queryset = CarBrand.objects.all()
    serializer_class = CarBrandSerializer
    filterset_class = CarBrandListFilterSet
    permission_classes = (
        permissions.IsAuthenticated,
    )


class CarBrandRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = CarBrand.objects.all()
    serializer_class = CarBrandSerializer
    permission_classes = (
        permissions.IsAuthenticated,
    )

class CarModelListCreate(generics.ListCreateAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarModelSerializer
    filterset_class = CarModelListFilterSet
    permission_classes = (
        permissions.IsAuthenticated,
    )

class CarModelRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarModelSerializer
    permission_classes = (
        permissions.IsAuthenticated,
    )