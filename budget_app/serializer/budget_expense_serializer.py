from rest_framework import serializers
from budget_app.models import BudgetExpense


class BudgetExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = BudgetExpense
        fields = ['id','amount', 'category', 'description']