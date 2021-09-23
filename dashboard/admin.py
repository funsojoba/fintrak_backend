from django.contrib import admin

# from django.contrib.auth.models import User
from authentication.models.user import User
from expense_app.models import Expense
from income_app.models import Income
from budget_app.models import BudgetExpense, BudgetIncome, TotalBudget


admin.site.register(User)
admin.site.register(Expense) 
admin.site.register(Income)
admin.site.register(BudgetExpense)
admin.site.register(BudgetIncome)
admin.site.register(TotalBudget)
