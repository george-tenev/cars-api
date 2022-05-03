from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('cars_app.accounts.urls')),
    path('', include('cars_app.cars_api.urls')),
    path('api-auth/', include('rest_framework.urls')),

]
