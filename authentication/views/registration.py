from decouple import config

from rest_framework.views import APIView

from lib.response import Response
from authentication.auth_utils.get_otp import create_random
from rest_framework import status

from authentication.serializers.register_serializer import RegisterSerializer
from authentication.models.user import User

from notifications.services import EmailServices



class RegisterView(APIView):
    serializer_class = RegisterSerializer
    def post(self, request):
        data = request.data
        serializer = RegisterSerializer(data=data)

        first_name = data.get('first_name', '')
        last_name = data.get('last_name', '')
        email = data.get('email', '')
        password = data.get('password', '')

        if not serializer.is_valid():
            return Response(errors=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        otp = create_random()
        EMAIL_VERIFICATION_URL = config('EMAIL_VERIFICATION_URL')
        verification_link=f"{EMAIL_VERIFICATION_URL}?email={email}"
        context={
            "first_name":first_name,
            "last_name":last_name,
            "otp":otp,
            "verification_link":verification_link
        }
        EmailServices.send_async(
            template="register.html",
            subject="Verify Email",
            recipients=[email],
            context=context
        )
        user = User.objects.create(first_name=first_name, last_name=last_name, email=email, password=password, otp=otp)
        user.set_password(password)
        user.save()

        return Response(data={"message":"Confirmation email sent to your email"}, status=status.HTTP_201_CREATED)
