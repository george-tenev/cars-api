from django.contrib import admin

from cars_app.cars_api.models import UserCar, CarBrand, CarModel


@admin.register(UserCar)
class UserCarAdmin(admin.ModelAdmin):
    pass


@admin.register(CarBrand)
class CarBrandAdmin(admin.ModelAdmin):
    pass


@admin.register(CarModel)
class CarModelAdmin(admin.ModelAdmin):
    pass
