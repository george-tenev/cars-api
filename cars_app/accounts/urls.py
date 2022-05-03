from django.urls import path

from cars_app.accounts import views

urlpatterns = [
    path('register/', views.UserCreate.as_view(), name='register'),
    path('profiles/', views.ProfilesList.as_view(), name='profiles list'),
    path('profiles/<int:pk>', views.RetrieveUpdateDeleteProfile.as_view(), name='profile_retrieve_update_delete')
]
