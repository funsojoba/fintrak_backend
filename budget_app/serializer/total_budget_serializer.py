from rest_framework import serializers
from budget_app.models import TotalBudget


class TotalBudgetSerializer(serializers.ModelSerializer):
    class Meta:
        field = '__all__'
        model = TotalBudget