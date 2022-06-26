from datetime import datetime
from rest_framework.views import APIView
from rest_framework import permissions, status

from lib.response import Response
from user_app.models import UserProfile
from user_app.serializer import UserProfileSerializer



class UpdateUserProfileView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserProfileSerializer

    def patch(self, request):
        user = request.user
        user_profile = UserProfile.objects.filter(user=user).first()
        serializer = self.serializer_class(user_profile, data=request.data)
        if serializer.is_valid():
            user_profile.date_of_birth = serializer.validated_data['date_of_birth'] or user_profile.date_of_birth
            user_profile.phone = serializer.validated_data['phone'] or user_profile.phone
            user_profile.address = serializer.validated_data['address'] or user_profile.address
            user_profile.prefered_currency = serializer.validated_data['prefered_currency'] or user_profile.prefered_currency
            user_profile.save()
            return Response(data=UserProfileSerializer(user_profile).data, status=status.HTTP_200_OK)
        return Response(errors=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
