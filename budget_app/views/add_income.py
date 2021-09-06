from rest_framework.views import APIView
from rest_framework import permissions, status
from datetime import datetime
from lib.response import Response

from budget_app.models import BudgetExpense, BudgetIncome, TotalBudget
from budget_app.serializer.budget_income_serializer import BudgetIncomeSerializer
from budget_app.serializer.total_budget_serializer import TotalBudgetSerializer


class AddIncome(APIView):
    serializer_class = BudgetIncomeSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request):
        data = request.data
        owner = request.user
        
        amount = data.get('amount', '')
        month = datetime.now().month
        source = data.get('source', '')
        description = data.get('description', '')

        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)

        add_income = BudgetIncome.objects.create(owner=owner, amount=amount, source=source, month=month, description=description)

        total_budget = TotalBudget.objects.filter(owner=request.user, month=datetime.now().month).first()
        total_budget_data = None

        if total_budget:
            total_budget.total += int(amount)
            total_budget_data = TotalBudgetSerializer(total_budget)
            total_budget.save()
        else:
            total_budget_created = TotalBudget.objects.create(owner=request.user, month=datetime.now().month, total=amount)
            total_budget_created.save()
            total_budget_data(total_budget_created)
        
        return Response(data={"data": serializer.data, "total":total_budget_data}, status=status.HTTP_201_CREATED)
