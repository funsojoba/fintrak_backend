from rest_framework import serializers
from .models import UserProfile
from authentication.models.User import User


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['phone', 'address', 'date_of_birth', 'prefered_currency']
        model = UserProfile


class AvatarSerializer(serializers.Serializer):
    avatar = serializers.FileField()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id', 'first_name', 'last_name', 'email', 'avatar']
        model = User


class ChangePasswordSerializer(serializers.Serializer):
    current_password = serializers.CharField(max_length=20)
    new_password = serializers.CharField(max_length=20)
