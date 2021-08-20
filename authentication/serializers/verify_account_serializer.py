from rest_framework import serializers


class VerifyAccountSerializer(serializers.Serializer):
    otp = serializers.CharField(max_length=8)
    email = serializers.EmailField()
    