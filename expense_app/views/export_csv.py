import csv
from datetime import datetime

from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework import permissions

from income_app.models import Income
from expense_app.models import Expense


class ExportExpenseCsv(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        response = HttpResponse(content_type='text/csv')
        writer = csv.writer(response)
        writer.writerow(['Amount', 'Category', 'Description', 'Date'])

        current_month = datetime.now().month
        expense = Expense.objects.filter(
            owner=request.user, expense_date__month=current_month).values_list('amount', 'category', 'description', 'expense_date')

        for item in expense:
            writer.writerow(item)

        response['Content-Description'] = f'attachment; filename=income-{str(datetime.now())}.csv'

        return response
