import uuid
from django.db import models
from django.conf import settings


class Income(models.Model):

    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE)
    amount = models.DecimalField(decimal_places=2, max_digits=20)
    source = models.CharField(max_length=245)
    description = models.CharField(max_length=255)
    income_date = models.DateField()
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.amount)
