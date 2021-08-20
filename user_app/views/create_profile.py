from rest_framework.views import APIView
from rest_framework import permissions, status

from lib.response import Response
from user_app.models import UserProfile
from user_app.serializer import UserProfileSerializer


class CreateUserProfileView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserProfileSerializer

    def post(self, request):
        data = request.data
        serializer = UserProfileSerializer(data=data)

        serializer.is_valid(raise_exception=True)

        user = request.user
        phone = data.get('phone', '')
        address = data.get('address', '')
        date_of_birth = data.get('date_of_birth')
        prefered_currency = data.get('prefered_currency', '')

        user_profile = UserProfile.objects.filter(user=user)

        if not user_profile.exists():
            create_profile = UserProfile.objects.create(user=user, phone=phone, address=address, date_of_birth=date_of_birth, prefered_currency=prefered_currency)
            create_profile.save()
            return Response(data=dict(data=serializer.data), status=status.HTTP_201_CREATED)
        else:
            user_profile_db = UserProfile.objects.get(user=user)
            
            if not phone:
                phone = user_profile_db.phone
                
            if not address:
                address = user_profile_db.address
            
            if not date_of_birth:
                date_of_birth = user_profile_db.date_of_birth
            
            if not prefered_currency:
                prefered_currency = user_profile_db.prefered_currency

            user_profile_db.phone = phone
            user_profile_db.address = address
            user_profile_db.date_of_birth = date_of_birth
            user_profile_db.prefered_currency = prefered_currency
            user_profile_db.save()
            return Response(data=dict(data=serializer.data), status=status.HTTP_200_OK)
