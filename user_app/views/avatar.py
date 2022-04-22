
from decouple import config

from rest_framework.views import APIView
from rest_framework import permissions, status

from lib.response import Response
from authentication.models.User import User
from user_app.serializer import AvatarSerializer

from lib.cloudinary import CloudinaryManager


class AvatarView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = AvatarSerializer

    def post(self, request):
        user = User.objects.get(id=request.user.id)
        serializer = AvatarSerializer(data=request.data)

        avatar = request.data.get('avatar', '')
        serializer.is_valid()
        if not avatar:
            return Response(errors=dict(avatar_error='Please input a proper file format'), status=status.HTTP_400_BAD_REQUEST)

        avatar_url = CloudinaryManager.upload_image(avatar, config('FOLDER_NAME'))
        user.avatar = avatar_url
        user.save()

        serializer_dict = dict(serializer.data)
        serializer_dict['avatar'] = avatar_url

        return Response(data=serializer_dict, status=status.HTTP_201_CREATED)
