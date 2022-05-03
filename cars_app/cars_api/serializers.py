from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from cars_app.accounts.admin import UserModel
from cars_app.cars_api.models import CarBrand, CarModel, UserCar


class UserForUserCarSerializer(ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['username', 'pk']


class CarBrandSerializer(ModelSerializer):
    class Meta:
        model = CarBrand
        fields = ['name']


class CarModelSerializer(ModelSerializer):
    class Meta:
        model = CarModel
        fields = ['name']


class UserCarSerializer(ModelSerializer):
    user = serializers.SlugRelatedField(
        slug_field='username',
        queryset = UserModel.objects.all()
     )
    car_brand = serializers.SlugRelatedField(
        slug_field='name',
        queryset = CarBrand.objects.all()
     )
    car_model = serializers.SlugRelatedField(
        slug_field='name',
        queryset = CarModel.objects.all()
     )


    class Meta:
        model = UserCar
        fields = ['first_reg', 'odometer', 'user', 'car_brand', 'car_model']