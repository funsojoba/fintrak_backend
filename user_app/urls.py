from django.urls import path
from .views.user_profile import GetUserProfile
from .views.create_profile import UpdateUserProfileView
from .views.delete_profile import DeleteUserProfile
from .views.avatar import AvatarView
from .views.change_password import ChangePasswordView

urlpatterns = [
    path('', GetUserProfile.as_view(), name='user-profile'),
    path('update', UpdateUserProfileView.as_view(), name='update-profile'),
    path('delete', DeleteUserProfile.as_view(), name='delete-profile'),
    path('avatar', AvatarView.as_view(), name='avatar'),
    path('change-password', ChangePasswordView.as_view(), name='change-password')
]
