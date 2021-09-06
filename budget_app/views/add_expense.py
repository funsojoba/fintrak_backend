from datetime import datetime

from rest_framework import views, status, permissions

from lib.response import Response
from budget_app.serializer.budget_expense_serializer import BudgetExpenseSerializer
from budget_app.models import BudgetExpense, TotalBudget


class AddExpense(views.APIView):
    permission_classes = [permissions.IsAuthenticated]
    seriailizer_class = BudgetExpenseSerializer

    def post(self, request):
        owner = request.user
        data = request.data

        amount = data.get('amount', '')
        month = datetime.now().month
        category = data.get('category', '')
        description = data.get('description', '')

        serializer = self.seriailizer_class(data=data)
        serializer.is_valid(raise_exception=True)


        total_budget = TotalBudget.objects.filter(owner=owner, month=month).first()

        if not total_budget:
            return Response(errors={"budget_error":"You need to add expected income first"}, status=status.HTTP_400_BAD_REQUEST)
        
        total_budget.total -= int(amount)
        total_budget.save()

        BudgetExpense.objects.create(owner=owner, month=month, amount=amount, category=category, description=description)
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)