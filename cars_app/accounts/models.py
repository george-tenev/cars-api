from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.validators import MinLengthValidator
from django.db import models
from django_softdelete.models import SoftDeleteModel

from cars_app.accounts.managers import CarsUserManager


class CarsUser(SoftDeleteModel, AbstractBaseUser, PermissionsMixin):
    username_validator = UnicodeUsernameValidator()
    USERNAME_MAX_LENGTH = 150
    USERNAME_UNIQUE_ERROR_MESSAGE = "A user with that username already exists."
    username = models.CharField(
        max_length=USERNAME_MAX_LENGTH,
        unique=True,
        validators=[username_validator],
        error_messages={"unique": USERNAME_UNIQUE_ERROR_MESSAGE, },
    )

    is_staff = models.BooleanField(
        default=False,
    )

    date_joined = models.DateTimeField(
        auto_now_add=True,
    )

    USERNAME_FIELD = 'username'
    objects = CarsUserManager()



class Profile(SoftDeleteModel, models.Model):
    FIRST_NAME_MIN_LENGTH = 2
    FIRST_NAME_MAX_LENGTH = 100
    LAST_NAME_MIN_LENGTH = 2
    LAST_NAME_MAX_LENGTH = 100
    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=[
            MinLengthValidator(FIRST_NAME_MIN_LENGTH),
        ]
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        validators=[
            MinLengthValidator(LAST_NAME_MIN_LENGTH),
        ]
    )
    date_of_birth = models.DateField()
    email = models.EmailField()

    user = models.OneToOneField(
        CarsUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    def __str__(self):
        return self.first_name

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

