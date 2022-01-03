from django.urls import path
from .views import DashboardView, ReportView

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('report', ReportView.as_view(), name='report')
]
