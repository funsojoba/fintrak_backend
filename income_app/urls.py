from django.urls import path

from income_app.views.add_income import AddIncomeView
from income_app.views.list_income import ListIncomeView
from income_app.views.edit_income import EditIncomeView
from income_app.views.delete_income import DeleteIncomeView
from income_app.views.export_csv import ExportIncomeCsv
from .views.detail import IncomeDetial

urlpatterns = [
    path('detail/<str:pk>', IncomeDetial.as_view(), name='add-income'),
    path('add', AddIncomeView.as_view(), name='add-income'),
    path('list', ListIncomeView.as_view(), name='list-income'),
    path('edit/<str:pk>', EditIncomeView.as_view(), name='edit-income'),
    path('delete/<str:pk>', DeleteIncomeView.as_view(), name='delete-income'),
    path('income-csv', ExportIncomeCsv.as_view(), name='income-csv'),
]
