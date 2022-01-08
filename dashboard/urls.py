from django.urls import path
from .views import DashboardView, ReportView, GeneratePDF, NewGeneratePdf

urlpatterns = [
    path('month/<str:month_id>', DashboardView.as_view(), name='dashboard'),
    path('report/<str:month_id>/<str:year_id>', ReportView.as_view(), name='report'),
    path('report-pdf', GeneratePDF.as_view(), name='report_pdf'),
    path('report-pdf-two', NewGeneratePdf.as_view(), name='report_pdf-two'),
]
