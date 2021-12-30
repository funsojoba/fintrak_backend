from rest_framework.views import APIView
from lib.response import Response
from rest_framework import status

from authentication.models.user import User
from authentication.serializers.reset_password_serializer import ResetPasswordSerializer
from authentication.auth_utils.get_otp import create_random

class ResetPasswordView(APIView):
    serializer_class = ResetPasswordSerializer

    def post(self, request):
        otp = request.GET.get('otp', '')
        email = request.GET.get('email', '')

        data = request.data
        password = data.get('password', '')
        confirm_password = data.get('confirm_password', '')

        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)

        if password != confirm_password:
            return Response(errors={"message": "password and confirm password must match"}, status=status.HTTP_400_BAD_REQUEST)

        db_user = User.objects.filter(email=email).first()

        if not db_user:
            return Response(errors={"message":"invalid reset-password link"}, status=status.HTTP_400_BAD_REQUEST)

        if db_user.otp != otp:
            return Response(errors={"message": "invalid reset-password link"}, status=status.HTTP_400_BAD_REQUEST)
        
        user.otp = create_random()
        user.set_password(password)
        user.save()
        return Response(data={"message":"password reset successfuly"}, status=status.HTTP_200_OK)