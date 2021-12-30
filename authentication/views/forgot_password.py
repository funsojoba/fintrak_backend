from decouple import config

from rest_framework.views import APIView
from rest_framework import status

from lib.response import Response
from authentication.auth_utils.get_otp import create_random
from authentication.models.user import User
from authentication.serializers.forgot_password_serializer import ForgotPasswordSerializer

from notifications.services import EmailServices


class ForgotPasswordView(APIView):
    serializer_class = ForgotPasswordSerializer

    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        email= data.get('email', '')

        serializer.is_valid(raise_exception=True)

        user = User.objects.filter(email=email).first()
        if not user:
            return Response(errors={"message":"user does not exist"}, status=status.HTTP_400_BAD_REQUEST)

        otp = user.otp

        RESET_EMAIL_URL = config('RESET_EMAIL_URL')
        # email_text = f'Follow the link below to reset your password'
        # email_body = f'Hi {user.first_name} {user.last_name}, \n {email_text} \n Visit <a href="{RESET_EMAIL_URL}' \
        #     f'?otp={otp}&email={email}">link</a> to verify'
        reset_password_link =f'{RESET_EMAIL_URL}?otp={otp}&email={email}'
        context = {
            "first_name":user.first_name,
            "last_name":user.last_name,
            "reset_password_link":reset_password_link
        }
        EmailServices.send_async(
            template='forgot_password.html', 
            subject='Reset Password', 
            recipients=[email], 
            context=context)
        
        # email_data = {
        #     "email_subject":"Reset Password",
        #     "email_body": email_body,
        #     "email_to":[email]
        # }
        # is_send_mail = MailUtil.send_mail(email_data)
        # if not is_send_mail:
        #     return Response({"error": "Email service is unavailable"}, status=status.HTTP_503_SERVICE_UNAVAILABLE)

        return Response(data={"message":"reset password link sent to your email"}, status=status.HTTP_200_OK)
        
