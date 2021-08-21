from django.urls import path

# from income_app.views.add_income import AddIncomeView
from income_app.views.list_income import ListIncomeView
from income_app.views.edit_income import EditIncomeView

urlpatterns = [
    path('list', ListIncomeView.as_view(), name='list-income'),
    path('edit/<str:pk>', EditIncomeView.as_view(), name='edit-income'),
]
