from rest_framework import serializers
from income_app.models import Income


class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = [ 'id', 'amount', 'source', 'description', 'income_date' ]