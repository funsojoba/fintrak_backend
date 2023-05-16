from drf_yasg.utils import swagger_auto_schema
from django.contrib.auth.hashers import check_password

from rest_framework import status
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from authentication.models.User import User
from user_app.serializer import UserSerializer

from lib.response import Response


from authentication.serializers.login_serializer import LoginSerializer
from authentication.docs import schema_example

class LoginUser(APIView):
    
    @swagger_auto_schema(
        request_body=LoginSerializer,
        operation_description="Allows users to login",
        operation_summary="Login users",
        tags=["Auth"],
        responses=schema_example.LOGIN_RESPONSE
    )
    def post(self, request):
        
        serializer = LoginSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(errors=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        user = User.objects.filter(email=serializer.validated_data['email']).first()
        
        if user:
            user_password = check_password(serializer.validated_data['password'], user.password)

            if not user_password:
                return Response(errors={"error": "invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)

            token = RefreshToken.for_user(user)
            data = {
                "user": UserSerializer(instance=user).data,
                "token": {"refresh": str(token), "access": str(token.access_token)},
            }
            return Response(data=data)
        return Response(
            errors={"error": "Invalid credentials"},
            status=status.HTTP_400_BAD_REQUEST,)