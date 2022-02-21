from drf_yasg.utils import swagger_auto_schema

from rest_framework.views import APIView
from rest_framework import status, permissions

from lib.response import Response

from authentication.auth_utils.get_otp import create_random
from authentication.models.User import User
from authentication.serializers.verify_account_serializer import VerifyAccountSerializer

class VerifyAccountView(APIView):
    serializer_class = VerifyAccountSerializer

    @swagger_auto_schema(
        request_body=VerifyAccountSerializer,
        operation_description="Allows user verify their account",
        operation_summary="Allows user verify their account",
    )
    def post(self, request):
        data = request.data
        otp = data.get('otp')
        email = data.get('email')

        user_db = User.objects.filter(email=email).first()

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        if not user_db:
            return Response(errors={"message":"User does not exist"}, status=status.HTTP_400_BAD_REQUEST)

        if user_db.otp == otp and user_db.email == email:
            user_db.otp = create_random()
            user_db.is_active = True
            user_db.save()
            return Response(data={"message":"Account activated successfully"})
        
        return Response(errors={"message":"Invalid activation credentials"}, status=status.HTTP_400_BAD_REQUEST)
        