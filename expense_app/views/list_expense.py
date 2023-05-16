from datetime import datetime
from django.db.models import Sum

from rest_framework import views, status, permissions

from lib.response import Response
from expense_app.models import Expense
from expense_app.serializers.expense_serializer import ExpenseSerializer
from user_app.models import UserProfile

class ListExpenseView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ExpenseSerializer

    def get(self, request):
        owner = request.user
        month_id = request.GET.get("month", datetime.now().month)

        expense = Expense.objects.filter(owner=owner)
        serializer = self.serializer_class(expense, many=True)
        data = serializer.data

        # expense per month
        expense_per_month = expense.filter(
            owner=owner, expense_date__month=month_id).order_by('-expense_date')
        current_month_serializer = self.serializer_class(expense_per_month, many=True)

        # total income
        total_expense = expense.filter(
            owner=owner, expense_date__month=month_id).aggregate(Sum('amount'))

        # sum by source group
        expense_by_category = expense.filter(owner=owner, expense_date__month=month_id).values(
            'category').annotate(category_total=Sum('amount'))

        user_currency = UserProfile.objects.filter(user=request.user).first()
        currency = user_currency.prefered_currency if user_currency else "$"

        data_response = {
            "expense_per_month": current_month_serializer.data,
            "total_expense": total_expense['amount__sum'] if total_expense['amount__sum'] else 0,
            "expense_by_category": expense_by_category,
            "currency":currency
        }
        return Response(data=data_response, status=status.HTTP_200_OK)
