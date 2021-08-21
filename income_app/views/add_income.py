from rest_framework.views import APIView
from rest_framework import permissions, status

from lib.response import Response
from income_app.serializers.income_serializer import IncomeSerializer
from income_app.models import Income

class AddIncomeView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = IncomeSerializer
    def post(self, request):
        owner = request.user
        data = request.data

        serializer = self.serializer_class(data=data)

        serializer.is_valid(raise_exception=True)

        amount = data.get('amount', '')
        source = data.get('source', '')
        description = data.get('description', '')
        income_date = data.get('income_date', '')

        income = Income.objects.create(owner = owner, amount=amount, source=source, description=description, income_date=income_date)

        return Response(data={"message":"success"}, status=status.HTTP_201_CREATED)
