from datetime import datetime
from django.db.models import Sum

from rest_framework.views import APIView
from rest_framework import permissions, status

from lib.response import Response
from budget_app.models import BudgetExpense, BudgetIncome, TotalBudget
from budget_app.serializer.budget_income_serializer import BudgetIncomeSerializer
from budget_app.serializer.budget_expense_serializer import BudgetExpenseSerializer
from budget_app.serializer.total_budget_serializer import TotalBudgetSerializer



class BudgetDashboard(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        income = BudgetIncome.objects.filter(month=datetime.now().month, owner=request.user)
        income_data = BudgetIncomeSerializer(income, many=True)

        total_income = BudgetIncome.objects.filter(owner=request.user, month=datetime.now().month).aggregate(Sum('amount'))
        total_income_data = total_income['amount__sum'] if total_income['amount__sum'] else 0

        expense = BudgetExpense.objects.filter(
            month=datetime.now().month, owner=request.user)
        expense_data = BudgetExpenseSerializer(expense, many=True)

        total_expense = BudgetExpense.objects.filter(owner=request.user, month=datetime.now().month).aggregate(Sum('amount'))
        total_expense_data = total_expense['amount__sum'] if total_expense['amount__sum'] else 0

        budget_balance_from_db = TotalBudget.objects.filter(
            month=datetime.now().month, owner=request.user).first()

        budget_balance = budget_balance_from_db.total if budget_balance_from_db else 0
        

        return Response(data={"income": income_data.data,
                            "expense": expense_data.data,
                            "budget_balance": budget_balance,
                            "total_income":total_income_data,
                            "total_expense":total_expense_data,
                            }, status=status.HTTP_200_OK)

