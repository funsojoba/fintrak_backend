from django.urls import path
from .views.user_profile import GetUserProfile
from .views.create_profile import CreateUserProfileView
from .views.delete_profile import DeleteUserProfile

urlpatterns = [
    path('', GetUserProfile.as_view(), name='user-profile'),
    path('create', CreateUserProfileView.as_view(), name='create-profile'),
    path('delete', DeleteUserProfile.as_view(), name='delete-profile'),
]
