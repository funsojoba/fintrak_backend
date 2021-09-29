from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions, status
from authentication.models.user import User


class DeleteUserProfile(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request):
        user = request.user

        db_user = User.objects.get(id=user.id)
        db_user.is_active = False
        db_user.save()
        return Response({"message":"account deleted"}, status=status.HTTP_204_NO_CONTENT)
