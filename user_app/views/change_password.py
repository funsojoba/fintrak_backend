from rest_framework.views import APIView
from rest_framework import permissions, status

from lib.response import Response
from user_app.models import UserProfile
from user_app.serializer import ChangePasswordSerializer
from authentication.models.User import User


class ChangePasswordView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ChangePasswordSerializer

    def post(self, request):
        user = request.user
        data = request.data
        user_detail = User.objects.get(id=user.id)
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        current_password = data.get('current_password')
        new_password = data.get('new_password')

        correct_current_password = user_detail.check_password(current_password)
        if not correct_current_password:
            return Response(errors={"message":"current password is not correct"}, status=status.HTTP_400_BAD_REQUEST)

        user_detail.set_password(new_password)
        user_detail.save()

        return Response(data={"message":"password reset successfully"}, status=status.HTTP_200_OK)

