from django.db.models import Sum

from datetime import datetime

from rest_framework import views, permissions, status

from lib.response import Response
from income_app.models import Income
from expense_app.models import Expense

from expense_app.serializers.expense_serializer import ExpenseSerializer
from income_app.serializers.income_serializer import IncomeSerializer

import pprint


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

        available_balance = sum_of_income['amount__sum'] - \
            sum_of_expenses['amount__sum']

        # TOP 3 INCOMES
        all_income = Income.objects.filter(
            owner=user, income_date__month=current_month).order_by('-created_at')
        all_income_serialized = IncomeSerializer(all_income, many=True)

        # TOP 3 EXPENSES
        all_expense = Expense.objects.filter(
            owner=user, expense_date__month=current_month).order_by('-created_at')
        all_expense_serialized = ExpenseSerializer(all_expense, many=True)

        days_range = [i for i in range(1, 32)]

        expense_graph = {}
        date_list = [(i.expense_date).day for i in all_expense]

        for i in days_range:
            for j in all_income:
                if i == (j.income_date).day:
                    expense_graph[i]=j.amount

        print("********PRINGINT**********")
        pprint.pprint(expense_graph)

        results = {
            "total_transaction": total_transaction,
            "sum_of_income": sum_of_income,
            "sum_of_expenses": sum_of_expenses,
            "available_balance": available_balance,
            "top_income": all_income_serialized.data[0:3],
            "top_expense": all_expense_serialized.data[0:3]
        }

        return Response(data=results, status=status.HTTP_200_OK)
