import django_filters.rest_framework as django_filters
from django.contrib.auth import get_user_model

from cars_app.accounts.models import Profile
from cars_app.cars_api.models import UserCar


UserModel = get_user_model()

class ProfileFilterSet(django_filters.FilterSet):
    cars = django_filters.BaseInFilter(method='filter_cars')

    def filter_cars(self, queryset, name, value):
        cars = UserCar.objects.select_related('user').filter(car_brand__name__in=value)
        users = UserModel.objects.select_related('profile').filter(usercar__in=cars).distinct()
        profiles = Profile.objects.filter(user__in=users)
        return profiles

    class Meta:
        model = Profile
        fields = {
            'first_name': ['exact',],
            'last_name': ['exact',],
        }

