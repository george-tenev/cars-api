from django.contrib.auth import get_user_model
from django.db import models
from django_softdelete.models import SoftDeleteModel

UserModel = get_user_model()

class CarBrand(SoftDeleteModel):
    CAR_MAX_LENGTH = 150
    name = models.CharField(max_length=CAR_MAX_LENGTH)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class CarModel(SoftDeleteModel):
    CAR_MODEL_MAX_LENGTH = 150
    name = models.CharField(max_length=CAR_MODEL_MAX_LENGTH)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    car_brand = models.ForeignKey(
        CarBrand,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name

class UserCar(SoftDeleteModel):
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE
    )
    car_brand = models.ForeignKey(
        CarBrand,
        on_delete=models.CASCADE,
    )
    car_model = models.ForeignKey(
        CarModel,
        on_delete=models.CASCADE,
    )
    first_reg = models.DateField()
    odometer = models.PositiveBigIntegerField()

    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def car_name(self):
        return f'{self.car_brand.name} {self.car_model.name}'

    def __str__(self):
        return self.car_name