from typing import List
from django.urls import path

from .views.list_expense import ListExpenseView

urlpatterns = [
    path('list', ListExpenseView.as_view(), name="expense-list")
]
