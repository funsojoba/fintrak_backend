from django.urls import path
from .views.registration import RegisterView


urlpatterns = [
    path('register', RegisterView.as_view(), name='register')
]


