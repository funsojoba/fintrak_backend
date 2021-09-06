from django.contrib import admin

# from django.contrib.auth.models import User
from authentication.models import user
from expense_app.models import Expense
from income_app.models import Income
from budget_app.models import BudgetExpense, BudgetIncome, TotalBudget


admin.site.register((user.User, Expense, Income,
                    BudgetExpense, BudgetIncome, TotalBudget))
