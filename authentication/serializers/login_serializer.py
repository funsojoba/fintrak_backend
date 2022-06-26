from rest_framework import serializers


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField() # TODO: Add a validator to check if the password is at least 8 characters long