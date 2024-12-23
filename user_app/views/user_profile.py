from rest_framework.views import APIView
from rest_framework import permissions, status

from lib.response import Response
from user_app.models import UserProfile
from user_app.serializer import UserProfileSerializer, UserSerializer
from authentication.models.User import User


class GetUserProfile(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        user = request.user
        user_profile = UserProfile.objects.filter(user=user).first()

        profile_serializer = UserProfileSerializer(user_profile)

        return Response(data={'profile':profile_serializer.data}, status=status.HTTP_200_OK)
