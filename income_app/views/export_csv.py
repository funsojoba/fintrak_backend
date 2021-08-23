import csv
from datetime import datetime

from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework import permissions

from income_app.models import Income


class ExportIncomeCsv(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        response = HttpResponse(content_type='text/csv')
        writer = csv.writer(response)
        writer.writerow(['Amount', 'Source', 'Description', 'Date'])

        current_month = datetime.now().month
        income = Income.objects.filter(
            owner=request.user, income_date__month=current_month).values_list('amount', 'source', 'description', 'income_date')

        for item in income:
            writer.writerow(item)

        response['Content-Description'] = f'attachment; filename=income-{str(datetime.now())}.csv'

        return response
