from rest_framework import serializers
from budget_app.models import BudgetIncome


class BudgetIncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BudgetIncome
        fields = ['amount', 'source', 'description']