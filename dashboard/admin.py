from django.contrib import admin

# from django.contrib.auth.models import User
from authentication.models.User import User
from budget_app.models import BudgetExpense, BudgetIncome, TotalBudget



admin.site.register(User)


admin.site.register(BudgetExpense)
admin.site.register(BudgetIncome)
admin.site.register(TotalBudget)
