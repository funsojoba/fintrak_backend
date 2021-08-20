from django.urls import path
from .views.registration import RegisterView
from .views.verify_account import VerifyAccountView
from .views.forgot_password import ForgotPasswordView
from .views.reset_password import ResetPasswordView


urlpatterns = [
    path('register', RegisterView.as_view(), name='register'),
    path('verify-account', VerifyAccountView.as_view(), name="verify-account"),
    path('forgot-password', ForgotPasswordView.as_view(), name="forgot-password"),
    path('reset-password', ResetPasswordView.as_view(), name="reset-password"),
]


