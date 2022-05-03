from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from cars_app.cars_api.models import CarBrand, CarModel, UserCar


class UserCarForProfileListSerializer(ModelSerializer):
    car_brand = serializers.SlugRelatedField(
        slug_field='name',
        queryset=CarBrand.objects.all()
    )
    car_model = serializers.SlugRelatedField(
        slug_field='name',
        queryset=CarModel.objects.all()
    )

    class Meta:
        model = UserCar
        fields = ['first_reg', 'odometer', 'car_brand', 'car_model']