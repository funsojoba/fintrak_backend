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

        expense_query = Expense.objects.filter(owner=owner)
        serializer = self.serializer_class(expense_query, many=True)
        data = serializer.data

        

        # expense per month
        current_month = datetime.now().month
        expense_per_month = Expense.objects.filter(
            owner=owner, expense_date__month=current_month)
        current_month_serializer = self.serializer_class(
            expense_per_month, many=True)

        # total income
        total_expense = Expense.objects.filter(
            owner=owner, expense_date__month=current_month).aggregate(Sum('amount'))

        # sum by source group
        expense_by_category = Expense.objects.filter(owner=owner, expense_date__month=current_month).values(
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
