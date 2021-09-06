from django.urls import path

from .views.add_income import AddIncome
from .views.dashboard import BudgetDashboard

urlpatterns = [
    path('', BudgetDashboard.as_view(), name='budget_dashboard'),
    path('income', AddIncome.as_view(), name='budget_income'),
]
