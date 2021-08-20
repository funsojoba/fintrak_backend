from django.urls import path
from .views.registration import RegisterView
from .views.verify_account import VerifyAccountView


urlpatterns = [
    path('register', RegisterView.as_view(), name='register'),
    path('verify-account', VerifyAccountView.as_view(), name="verify-account"),
]


