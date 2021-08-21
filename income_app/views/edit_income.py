from rest_framework.views import APIView
from rest_framework import permissions, status

from lib.response import Response
from income_app.models import Income
from income_app.serializers.income_serializer import IncomeSerializer


class EditIncomeView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = IncomeSerializer

    def post(self, request, pk):
        income = Income.objects.get(id=pk)
        serializer = self.serializer_class(income)

        data = request.data

        amount = data.get('amount', '')
        source = data.get('source', '')
        description = data.get('description', '')
        income_date = data.get('income_date', '')

        # for k, v in data.items():
        #     if not v:
        #         data[k] = serializer[k]

        if not amount:
            amount = income.amount

        if not source:
            source = income.source

        if not description:
            description = income.description

        if not income_date:
            income_date = income.income_date

        income.amount = amount
        income.source = source
        income.description = description
        income.income_date = income_date
        income.save()
        return Response(data={"message": "success"}, status=status.HTTP_200_OK)
