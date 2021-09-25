from lib.response import Response

from rest_framework import status, permissions, views

from budget_app.models import BudgetIncome, TotalBudget
from budget_app.serializer.budget_income_serializer import BudgetIncomeSerializer


class EditAddIncome(views.APIView):
    permissions = [permissions.IsAuthenticated]
    serializer_class = BudgetIncomeSerializer

    def post(self, request, id):
        owner = request.user
        data = request.data
        total_budget = TotalBudget.objects.filter(owner=owner, id=id).first()

        amount = data.get('amount', '')
        month = total_budget.month
        source = data.get('source', '')
        description = data.get('description', '')
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)

        BudgetIncome.objects.create(owner=owner, amount=amount, source=source, description=description, month=month)
        total_budget.total_budget_income += int(amount)
        total_budget.total += int(amount)
        total_budget.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)
