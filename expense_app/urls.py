from typing import List
from django.urls import path

from .views.list_expense import ListExpenseView
from .views.add_expense import AddExpenseView
from .views.edit_expense import EditExpenseView
from .views.export_csv import ExportExpenseCsv

urlpatterns = [
    path('list', ListExpenseView.as_view(), name="expense-list"),
    path('add', AddExpenseView.as_view(), name="add-list"),
    path('edit/<str:pk>', EditExpenseView.as_view(), name="edit-list"),
    path('expense-csv', ExportExpenseCsv.as_view(), name="expense-csv"),
]
