from django.urls import path
from .views import DashboardView, ReportView, GeneratePDF, NewGeneratePdf

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('report', ReportView.as_view(), name='report'),
    path('report-pdf', GeneratePDF.as_view(), name='report_pdf'),
    path('report-pdf-two', NewGeneratePdf.as_view(), name='report_pdf-two'),
]
