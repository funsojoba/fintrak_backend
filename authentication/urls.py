from django.urls import path
from .views.registration import RegisterView
from .views.verify_account import VerifyAccountView
from .views.forgot_password import ForgotPasswordView
from .views.reset_password import ResetPasswordView
from .views.login import LoginUser
from .views.webhook import WebHookView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('register', RegisterView.as_view(), name='register'),
    path('login', LoginUser.as_view(), name='login'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('verify-account', VerifyAccountView.as_view(), name="verify-account"),
    path('forgot-password', ForgotPasswordView.as_view(), name="forgot-password"),
    path('reset-password', ResetPasswordView.as_view(), name="reset-password"),
    path('webhook', WebHookView.as_view(), name="webhook"),
]


