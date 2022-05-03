from django.contrib import admin
from django.contrib.auth import get_user_model

from cars_app.accounts.models import Profile

UserModel = get_user_model()

@admin.register(Profile)
class AppUserAdmin(admin.ModelAdmin):
    pass

@admin.register(UserModel)
class AppUserAdmin(admin.ModelAdmin):
    pass

