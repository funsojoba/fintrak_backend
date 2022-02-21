import cloudinary.uploader
from decouple import config

from rest_framework.views import APIView
from rest_framework import permissions, status

from lib.response import Response
from authentication.models.User import User
from user_app.serializer import AvatarSerializer


class AvatarView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = AvatarSerializer

    def post(self, request):
        user = User.objects.get(id=request.user.id)
        data = request.data
        serializer = AvatarSerializer(data=data)

        avatar = data.get('avatar', '')
        serializer.is_valid()
        if not avatar:
            return Response(errors=dict(avatar_error='Please input a proper file format'), status=status.HTTP_400_BAD_REQUEST)

        valid_extension = ['jpg', 'png', 'jpeg', 'JPEG', 'SVG', 'webp']

        if avatar.name.split('.')[-1] not in valid_extension:
            return Response(errors=dict(file_format_error="Please input a proper image file"), status=status.HTTP_400_BAD_REQUEST)

        upload_image = cloudinary.uploader.upload(avatar, folder=config(
            'FOLDER_NAME'), user_filename=True, overwrite=True)

        upload_image_url = upload_image.get('url')
        user.avatar = upload_image_url
        user.save()

        serializer_dict = dict(serializer.data)
        serializer_dict['avatar'] = upload_image_url

        return Response(data=serializer_dict, status=status.HTTP_201_CREATED)
