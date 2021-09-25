from django.urls import path

from .views.add_income import AddIncome
from .views.dashboard import BudgetDashboard
from .views.add_expense import AddExpense
from .views.budget_detail import BudgetDetailView
from .views.edit_add_income import EditAddIncome
from .views.edit_add_expense import EditAddExpense
from .views.delete_budget_income import DeleteBudgetIncome
from .views.delete_budget_expense import DeleteBudgetExpense

urlpatterns = [
    path('', BudgetDashboard.as_view(), name='budget_dashboard'),
    path('income', AddIncome.as_view(), name='budget_income'),
    path('expense', AddExpense.as_view(), name='budget_expense'),
    path('detail/<str:pk>', BudgetDetailView.as_view(), name='budget_detail'),
    path('edit-add-income/<str:id>', EditAddIncome.as_view(), name='edit_add_income'),
    path('edit-add-expense/<str:id>', EditAddExpense.as_view(), name='edit_add_expense'),
    path('delete-budget-income/<str:pk>', DeleteBudgetIncome.as_view(), name='delete_budget_income'),
    path('delete-budget-expense/<str:pk>',DeleteBudgetExpense.as_view(), name='delete_budget_expense'),
]
