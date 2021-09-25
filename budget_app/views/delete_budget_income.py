from lib.response import Response

from rest_framework import views, status, permissions
from budget_app.models import  BudgetIncome, TotalBudget


class DeleteBudgetIncome(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        owner = request.user
        income_budget = BudgetIncome.objects.filter(owner=owner, id=pk).first()
        budget_amount = income_budget.amount
        budget_month = income_budget.month

        total_budget = TotalBudget.objects.filter(owner=owner, month=budget_month).first()
        total_budget.total -= budget_amount
        total_budget.total_budget_income -= budget_amount
        total_budget.save()
        income_budget.delete()
        return Response(data={"status":"deleted"}, status=status.HTTP_204_NO_CONTENT)