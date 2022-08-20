from drf_yasg.utils import swagger_auto_schema
from django.contrib.auth.hashers import check_password

from rest_framework import status
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from authentication.models.User import User
from user_app.serializer import UserSerializer

from lib.response import Response


from authentication.serializers.login_serializer import LoginSerializer

from authentication.service import NotificationPreferenceService

class WebHookView(APIView):
    
    @swagger_auto_schema(
        operation_description="Webhook for notification preferences",
        operation_summary="Webhook for notification preferences",
    )
    def get(self, request):
        
        serializer = LoginSerializer(data=request.data)
        service_response = NotificationPreferenceService.update_preference(request)
        print("*****")
        print(service_response)
        return Response(
            data={"onaga":"onaga"}
        )