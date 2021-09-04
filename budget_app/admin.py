from django.contrib import admin
from .models import BudgetExpense, BudgetIncome

admin.site.register((BudgetIncome, BudgetExpense))
