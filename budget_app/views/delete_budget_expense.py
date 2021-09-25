from lib.response import Response

from rest_framework import views, status, permissions
from budget_app.models import  BudgetExpense, TotalBudget


class DeleteBudgetExpense(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        owner = request.user
        expense_budget = BudgetExpense.objects.filter(owner=owner, id=pk).first()
        budget_amount = expense_budget.amount
        budget_month = expense_budget.month

        total_budget = TotalBudget.objects.filter(owner=owner, month=budget_month).first()
        total_budget.total += budget_amount
        total_budget.total_budget_expense -= budget_amount
        total_budget.save()
        expense_budget.delete()
        return Response(data={"status":"deleted"}, status=status.HTTP_204_NO_CONTENT)