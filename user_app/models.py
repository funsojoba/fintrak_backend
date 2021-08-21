import uuid
from django.db import models
from django.conf import settings


class UserProfile(models.Model):

    DEFAULT_CURRENCY = 'USD - $'
    
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone = models.CharField(max_length=256, blank=True, null=True)
    address = models.CharField(max_length=256, blank=True, null=True)
    date_of_birth = models.DateField(null=True, blank=True)
    prefered_currency = models.CharField(max_length=256, default=DEFAULT_CURRENCY)

    def __str__(self):
        return str(self.user) +'\'s profile'