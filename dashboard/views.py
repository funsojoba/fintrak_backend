from datetime import datetime
from django.db.models import Sum

from rest_framework import views, permissions, status

from lib.response import Response
from income_app.models import Income
from expense_app.models import Expense
from expense_app.serializers.expense_serializer import ExpenseSerializer
from income_app.serializers.income_serializer import IncomeSerializer


class DashboardView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        current_month = datetime.now().month

        # TOTAL TRANSACTIONS
        income = Income.objects.filter(
            owner=user, income_date__month=current_month)
        expense = Expense.objects.filter(
            owner=user, expense_date__month=current_month)

        total_transaction = income.count() + expense.count()

        # SUM OF INCOME
        sum_of_income = Income.objects.filter(
            owner=user, income_date__month=current_month).aggregate(Sum('amount'))

        # SUM OF EXPENSES
        sum_of_expenses = Expense.objects.filter(
            owner=user, expense_date__month=current_month).aggregate(Sum('amount'))
        
        sum_of_expenses_amount = sum_of_expenses['amount__sum'] if sum_of_expenses['amount__sum'] else 0
        sum_of_income_amount = sum_of_income['amount__sum'] if sum_of_income['amount__sum'] else 0

        available_balance = sum_of_income_amount - sum_of_expenses_amount

        # TOP 3 INCOMES
        all_income = Income.objects.filter(
            owner=user, income_date__month=current_month).order_by('-created_at')
        all_income_serialized = IncomeSerializer(all_income, many=True)

        # TOP 3 EXPENSES
        all_expense = Expense.objects.filter(
            owner=user, expense_date__month=current_month).order_by('-created_at')
        all_expense_serialized = ExpenseSerializer(all_expense, many=True)


        # INCOME GRAPH DATA
        income_dict = {}

        for i in all_income:
            income_dict[i.income_date.day] = i.amount

        income_days = [i.income_date.day for i in all_income]

        income_graph_data = []

        for i in range(1, 32):
            if i in income_days:
                income_graph_data.append((i, income_dict[i]))
            income_graph_data.append((i, 0))

        #EXPENSE GRAPH DATA

        expense_dict = {}

        for i in all_expense:
            expense_dict[i.expense_date.day] = i.amount
        
        expense_days = [i.expense_date.day for i in all_expense]
        
        expense_graph_data = []

        for i in range(1, 32):
            if i in expense_days:
                expense_graph_data.append((i, expense_dict[i]))
            expense_graph_data.append((i, 0))

        results = {
            "total_transaction": total_transaction,
            "sum_of_income": sum_of_income['amount__sum'] if sum_of_income['amount__sum'] else 0,
            "sum_of_expenses": sum_of_expenses['amount__sum'] if sum_of_expenses['amount__sum'] else 0,
            "available_balance": available_balance,
            "top_income": all_income_serialized.data[0:3],
            "top_expense": all_expense_serialized.data[0:3],
            "income_graph_data": income_graph_data,
            "expense_graph_data": expense_graph_data
        }

        return Response(data=results, status=status.HTTP_200_OK)
