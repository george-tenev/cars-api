from django.urls import path, include, re_path

from cars_app.cars_api import views

urlpatterns = [
    path('cars/', views.UserCarsListCreate.as_view(), name='cars_create_list'),
    path('cars/<int:pk>', views.UserCarsRetrieveUpdateDestroy.as_view(), name='cars_retrieve_update_delete'),

    path('car_brands/', views.CarBrandListCreate.as_view(), name='car_brand_create_list'),
    path('car_brands/<int:pk>', views.CarBrandRetrieveUpdateDestroy.as_view(), name='car_brand_retrieve_update_delete'),

    path('car_model/', views.CarModelListCreate.as_view(), name='car_model_create_list'),
    path('car_model/<int:pk>', views.CarModelRetrieveUpdateDestroy.as_view(), name='car_model_retrieve_update_delete')
]
