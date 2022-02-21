from decouple import config
from django.conf import settings
from drf_yasg.utils import swagger_auto_schema

from rest_framework.views import APIView
from rest_framework import status

from lib.response import Response
from authentication.auth_utils.get_otp import create_random
from authentication.models.User import User
from authentication.serializers.forgot_password_serializer import ForgotPasswordSerializer

from notifications.services import EmailServices


class ForgotPasswordView(APIView):
    serializer_class = ForgotPasswordSerializer

    @swagger_auto_schema(
        request_body=ForgotPasswordSerializer,
        operation_description="Allows user reset their password with their email",
        operation_summary="Allows user reset their password with their email",
    )
    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        email= data.get('email', '')

        serializer.is_valid(raise_exception=True)

        user = User.objects.filter(email=email).first()
        if not user:
            return Response(errors={"message":"user does not exist"}, status=status.HTTP_400_BAD_REQUEST)

        otp = user.otp

        FRONT_END_URL = settings.FRONT_END_URL
        RESET_EMAIL_URL = settings.RESET_EMAIL_URL
        
        reset_password_link =f"{FRONT_END_URL}{RESET_EMAIL_URL}?otp={otp}&email={email}"
        context = {
            "first_name":"user.first_name",
            "last_name":"user.last_name",
            "reset_password_link":reset_password_link
        }
        EmailServices.send_async(
            template='forgot_password.html', 
            subject='Reset Password', 
            recipients=[email], 
            context=context)
        print(reset_password_link)
        
        return Response(data={"message":"reset password link sent to your email"}, status=status.HTTP_200_OK)
        
