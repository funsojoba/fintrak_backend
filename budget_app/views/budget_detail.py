from lib.response import Response
from rest_framework import views, permissions, status

from budget_app.models import TotalBudget, BudgetIncome, BudgetExpense
from budget_app.serializer.total_budget_serializer import TotalBudgetSerializer
from budget_app.serializer.budget_income_serializer import BudgetIncomeSerializer
from budget_app.serializer.budget_expense_serializer import BudgetExpenseSerializer


class BudgetDetailView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk):
        owner = request.user
        budget = TotalBudget.objects.filter(owner=owner, id=pk).first()
        serializer = TotalBudgetSerializer(budget)

        income = BudgetIncome.objects.filter(owner=owner, month=budget.month)
        serialized_income = BudgetIncomeSerializer(income, many=True)

        expense = BudgetExpense.objects.filter(owner=owner, month=budget.month)
        serialized_expense = BudgetExpenseSerializer(expense, many=True)
        
        return Response(data={
                    'budget':serializer.data,
                    'income':serialized_income.data,
                    'expense':serialized_expense.data}, status=status.HTTP_200_OK)
