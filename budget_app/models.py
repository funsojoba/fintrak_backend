import uuid
from django.db import models
from django.conf import settings


class BudgetIncome(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE)
    amount = models.DecimalField(decimal_places=2, max_digits=20, default=0)
    source = models.CharField(max_length=245)
    month = models.CharField(max_length=254)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{str(self.amount)} - {self.month}'


class BudgetExpense(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE)
    amount = models.DecimalField(decimal_places=2, max_digits=20, default=0)
    month = models.CharField(max_length=254)
    category = models.CharField(max_length=245)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{str(self.amount)} - {self.month}'


class TotalBudget(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True)
    month = models.CharField(max_length=256)
    total_budget_income = models.DecimalField(
        decimal_places=2, max_digits=20, default=0)
    total_budget_expense = models.DecimalField(
        decimal_places=2, max_digits=20, default=0)
    total = models.DecimalField(decimal_places=2, max_digits=20, default=0)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.total)
