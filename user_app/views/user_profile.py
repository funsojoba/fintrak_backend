from rest_framework.views import APIView
from rest_framework import permissions, status

from lib.response import Response
from user_app.models import UserProfile
from user_app.serializer import UserProfileSerializer


class GetUserProfile(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        user = request.user
        user_profile = UserProfile.objects.filter(user=user)

        if not user_profile.exists():
            return Response(errors=dict(user_profile_error='No user profile yet'), status=status.HTTP_400_BAD_REQUEST)

        serializer_dict = UserProfileSerializer(user_profile[0])
        # serializer_dict.is_valid()
        return Response(data=dict(user_profile=serializer_dict.data), status=status.HTTP_200_OK)
