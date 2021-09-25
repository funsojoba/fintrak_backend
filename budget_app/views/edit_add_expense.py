from lib.response import Response

from rest_framework import status, permissions, views

from budget_app.models import TotalBudget, BudgetExpense
from budget_app.serializer.budget_expense_serializer import BudgetExpenseSerializer


class EditAddExpense(views.APIView):
    permissions = [permissions.IsAuthenticated]
    serializer_class = BudgetExpenseSerializer

    def post(self, request, id):
        owner = request.user
        data = request.data
        total_budget = TotalBudget.objects.filter(owner=owner, id=id).first()

        amount = data.get('amount', '')
        month = total_budget.month
        category = data.get('category', '')
        description = data.get('description', '')
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)

        BudgetExpense.objects.create(
            owner=owner, amount=amount, category=category, description=description, month=month)
        total_budget.total_budget_expense += int(amount)
        total_budget.total -= int(amount)
        total_budget.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)
