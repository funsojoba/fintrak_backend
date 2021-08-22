import uuid
from django.db import models
from django.conf import settings


class Expense(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE)
    amount = models.DecimalField(decimal_places=2, max_digits=20, default=0)
    description = models.CharField(max_length=256)
    category = models.CharField(max_length=240)
    expense_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.amount
