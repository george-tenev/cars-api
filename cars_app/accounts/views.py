from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework import permissions

from cars_app.accounts.filters import ProfileFilterSet
from cars_app.accounts.models import Profile
from cars_app.accounts.serializers import UserSerializer, ProfileSerializer

UserModel = get_user_model()


class UserCreate(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)


class ProfilesList(generics.ListAPIView):
    queryset = Profile.objects.select_related('user').prefetch_related('user__usercar_set').all()
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ProfileSerializer
    filterset_class = ProfileFilterSet


class RetrieveUpdateDeleteProfile(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (
        permissions.IsAuthenticated,
    )
