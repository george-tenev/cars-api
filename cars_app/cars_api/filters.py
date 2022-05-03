# import django_filters
import django_filters.rest_framework as django_filters

from cars_app.accounts.admin import UserModel
from cars_app.cars_api.models import UserCar, CarBrand, CarModel


class UserCarListFilterSet(django_filters.FilterSet):
    USERS_QS = UserModel.objects.all()

    user_id = django_filters.ModelMultipleChoiceFilter(
        field_name='user_id',
        queryset=USERS_QS
    )
    user = django_filters.ModelMultipleChoiceFilter(
        field_name='user__username',
        to_field_name='username',
        queryset=USERS_QS
    )
    owner_first_name = django_filters.CharFilter(field_name='user__profile__first_name')

    class Meta:
        model = UserCar
        fields = {
            'car_brand__name': ['istartswith', 'iexact'],
            'car_model__name': ['istartswith', 'iexact'],
            'first_reg': ['exact', 'year__gt', 'year__lt', 'in',],
            'odometer': ['exact', 'lt', 'gt']
        }


class CarBrandListFilterSet(django_filters.FilterSet):

    usercar__user_id = django_filters.NumberFilter(
        field_name='usercar__user_id',
        distinct=True
    )

    class Meta:
        model = CarBrand
        fields = {
            'name': ['istartswith', 'iexact'],
        }

class CarModelListFilterSet(django_filters.FilterSet):

    usercar__user_id = django_filters.NumberFilter(
        field_name='usercar__user_id',
        distinct=True
    )

    class Meta:
        model = CarModel
        fields = {
            'name': ['istartswith', 'iexact'],
            'car_brand__name': ['iexact', 'in']
        }




