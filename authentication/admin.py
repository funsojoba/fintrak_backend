from django.contrib import admin

from authentication.models.user import User
# from django.contrib.auth.models import User


admin.site.register(User)