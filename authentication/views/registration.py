from decouple import config

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status

from authentication.serializers.register_serializer import RegisterSerializer
from authentication.models.user import User
from authentication.auth_utils.get_otp import create_random
from authentication.auth_utils.send_mail import MailUtil

class RegisterView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer
    def post(self, request):
        data = request.data
        serializer = RegisterSerializer(data=data)

        first_name = data.get('first_name', '')
        last_name = data.get('last_name', '')
        email = data.get('email', '')
        password = data.get('password', '')

        if not serializer.is_valid():
            return Response({"error": serializer.errors, "data": None}, status=status.HTTP_400_BAD_REQUEST)

        user_from_db = User.objects.filter(email=email)
        if user_from_db.exists():
            return Response({"error":"Email already exist", "data":"null"}, status=status.HTTP_400_BAD_REQUEST)

        otp = create_random()
        EMAIL_VERIFICATION_URL = config('EMAIL_VERIFICATION_URL')
        email_text = f'Thank you for registering with us, \n\n Please visit the link below to activate your account'
        email_body = f'Hi {first_name} {last_name}, \n {email_text} \n Visit <a href="{EMAIL_VERIFICATION_URL}' \
            f'?otp={otp}&email={email}">link</a> to verify'

        email_data = {
            "email_subject":"Account verification",
            "email_body": email_body,
            "email_to":[email]
        }

        is_send_mail = MailUtil.send_mail(email_data)
        if not is_send_mail:
            return Response({"error":"Email service is unavailable"}, status=status.HTTP_503_SERVICE_UNAVAILABLE)

        user = User.objects.create(first_name=first_name, last_name=last_name, email=email, password=password, otp=otp)
        user.set_password(password)
        user.save()

        return Response({"message":"success"}, status=status.HTTP_201_CREATED)
