from datetime import datetime
from rest_framework.views import APIView
from rest_framework import permissions, status

from lib.response import Response
from user_app.models import UserProfile
from user_app.serializer import UserProfileSerializer



class CreateUserProfileView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserProfileSerializer

    def patch(self, request):
        user = request.user
        user_profile = UserProfile.objects.filter(user=user).first()
        serializer = self.serializer_class(user_profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data={"message": "success"}, status=status.HTTP_200_OK)
        return Response(errors={"message": "Failure"}, status=status.HTTP_400_BAD_REQUEST)
