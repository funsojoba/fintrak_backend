from django.contrib import admin

# from django.contrib.auth.models import User
from authentication.models.user import User


admin.site.register(User)
