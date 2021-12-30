from rest_framework import serializers
from authentication.models.user import User


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password']
    
    def validate_email(self, email):
        user = User.objects.filter(email=email).first()
        if user and not user.is_active:
            raise serializers.ValidationError("User is not activated yet")
        return email