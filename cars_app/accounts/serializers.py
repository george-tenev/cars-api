from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from cars_app.accounts.models import Profile
from cars_app.common.serializers import UserCarForProfileListSerializer

UserModel = get_user_model()


class ProfileForUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'email', 'date_of_brith')


class UserForProfileListSerializer(serializers.ModelSerializer):
    usercar_set = UserCarForProfileListSerializer(many=True, read_only=True)

    class Meta:
        model = UserModel
        fields = ['username', 'id', 'usercar_set']


class ProfileSerializer(serializers.ModelSerializer):
    user = UserForProfileListSerializer()

    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'email', 'user', 'date_of_birth')


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    profile = ProfileForUserSerializer(many=False)

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        user = UserModel.objects.create(
            username=validated_data['username'],
        )
        profile = Profile(user=user, **profile_data)
        profile.save()
        user.set_password(validated_data['password'])
        user.save()
        return user

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    class Meta:
        model = UserModel
        fields = ('username', 'password', 'password2', 'profile')
        extra_kwargs = {
            'password': {'write_only': True},
            'password2': {'write_only': True},
        }


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('username', 'password')
