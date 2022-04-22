import cloudinary.uploader
from lib.response import Response


class CloudinaryManager:
    
    @classmethod
    def upload_image(cls, file, folder):
        valid_extension = ['jpg', 'png', 'jpeg', 'JPEG', 'SVG', 'webp']

        if file.name.split('.')[-1] not in valid_extension:
            return Response(errors=dict(file_format_error="Please input a proper image file"), status=status.HTTP_400_BAD_REQUEST)

        upload_image = cloudinary.uploader.upload(file=file, folder=folder, user_filename=True, overwrite=True)
        return upload_image.get('url')