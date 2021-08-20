from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from authentication.auth_utils.get_otp import create_random
from authentication.models.user import User
from authentication.serializers.verify_account_serializer import VerifyAccountSerializer

class VerifyAccountView(APIView):
    serializer_class = VerifyAccountSerializer

    def post(self, request):
        data = request.data
        otp = data.get('otp')
        email = data.get('email')

        user_db = User.objects.filter(email=email)

        if not otp or not email:
            return Response({"message":"failure", "error":"Both otp and email are required"}, status=status.HTTP_400_BAD_REQUEST)

        if not user_db.exists():
            return Response({"message":"failure", "error":"User does not exist"}, status=status.HTTP_400_BAD_REQUEST)

        user = user_db[0]

        if user.otp == otp and user.email == email:
            user.otp = create_random()
            user.is_active = True
            user.save()
            return Response({"message":"success", "data":"Account activated successfully"})
        
        return Response({"message":"failure", "error":"Invalid activation credentials"}, status=status.HTTP_400_BAD_REQUEST)
        