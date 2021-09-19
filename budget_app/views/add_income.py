from django.db.models import Sum
from rest_framework.views import APIView
from rest_framework import permissions, status
from datetime import datetime
from lib.response import Response

from budget_app.models import BudgetIncome, TotalBudget
from budget_app.serializer.budget_income_serializer import BudgetIncomeSerializer


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

        BudgetIncome.objects.create(
            owner=owner, amount=amount, source=source, month=month, description=description)
        # total_budget_income = BudgetIncome.objects.filter(
            # owner=owner, month=month).aggregate(Sum('amount'))['amount__sum']

        total_budget = TotalBudget.objects.filter(
            owner=request.user, month=datetime.now().month).first()

        if total_budget:
            total_budget.total += int(amount)
            total_budget.total_budget_income += int(amount)
            total_budget.save()
        else:
            total_budget_created = TotalBudget.objects.create(
                owner=request.user, month=datetime.now().month, total=amount, total_budget_income=amount)
            total_budget_created.save()

        total_month_budget = TotalBudget.objects.filter(
            owner=owner, month=month).first()

        return Response(data=serializer.data, status=status.HTTP_201_CREATED)
