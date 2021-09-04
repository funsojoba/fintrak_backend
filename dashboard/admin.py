from django.contrib import admin

# from django.contrib.auth.models import User
from authentication.models.user import User
from expense_app.models import Expense
from income_app.models import Income
from budget_app.models import BudgetExpense, BudgetIncome


admin.site.register((User, Expense, Income, BudgetExpense, BudgetIncome))
