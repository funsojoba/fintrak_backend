from rest_framework.views import APIView
from rest_framework import permissions, status

from lib.response import Response
from user_app.models import UserProfile
from user_app.serializer import UserProfileSerializer
from authentication.models.user import User


class GetUserProfile(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        user = request.user
        user_profile = UserProfile.objects.filter(user=user).first()
        user_details = User.objects.filter(id=user.id).first()

        user_detail_info = {
            "first_name":user_details.first_name,
            "last_name":user_details.last_name,
            "email":user_details.email,
            "avatar":user_details.avatar,
        }

        user_profile_info = {}

        if not user_profile:
            user_detail_info['phone'] = ''
            user_detail_info['address'] = ''
            user_detail_info['date_of_birth'] = ''
        else:
            user_profile_info['phone'] = user_profile.phone
            user_profile_info['address'] = user_profile.address
            user_profile_info['date_of_birth'] = user_profile.date_of_birth
            user_profile_info['prefered_currency'] = user_profile.prefered_currency

        return Response(data={'user':user_detail_info, 'profile':user_profile_info}, status=status.HTTP_200_OK)
