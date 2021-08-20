from decouple import config

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from authentication.auth_utils.get_otp import create_random
from authentication.models.user import User
from authentication.serializers.forgot_password_serializer import ForgotPasswordSerializer
from authentication.auth_utils.send_mail import MailUtil

class ForgotPasswordView(APIView):
    serializer_class = ForgotPasswordSerializer

    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        email= data.get('email', '')

        serializer.is_valid(raise_exception=True)

        db_email = User.objects.filter(email=email)
        if not db_email.exists():
            return Response({"message":"failure", "error":"user does not exist"}, status=status.HTTP_400_BAD_REQUEST)

        user = db_email[0]
        otp = user.otp

        RESET_EMAIL_URL = config('RESET_EMAIL_URL')
        email_text = f'Follow the link below to reset your password'
        email_body = f'Hi {user.first_name} {user.last_name}, \n {email_text} \n Visit <a href="{RESET_EMAIL_URL}' \
            f'?otp={otp}&email={email}">link</a> to verify'

        email_data = {
            "email_subject":"Reset Password",
            "email_body": email_body,
            "email_to":[email]
        }
        is_send_mail = MailUtil.send_mail(email_data)
        if not is_send_mail:
            return Response({"error": "Email service is unavailable"}, status=status.HTTP_503_SERVICE_UNAVAILABLE)

        return Response({"message":"success", "info":"email sent"}, status=status.HTTP_200_OK)
        
