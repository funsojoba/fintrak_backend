from rest_framework import serializers
from .models import UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['phone', 'address', 'date_of_birth', 'prefered_currency']
        model = UserProfile