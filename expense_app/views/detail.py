from rest_framework.views import APIView
from rest_framework import permissions, status

from lib.response import Response
from expense_app.models import Expense
from expense_app.serializers.expense_serializer import ExpenseSerializer

from user_app.models import UserProfile


class ExpenseDetail(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ExpenseSerializer

    def get(self, request, pk):
        expense = Expense.objects.get(id=pk)
        serializer = ExpenseSerializer(expense)

        user_profile = UserProfile.objects.filter(user=request.user).first()
        currency = user_profile.currency if user_profile else '$'
        print(serializer.data)
        result = {
            "id":serializer.data['id'],
            "amount":serializer.data['amount'],
            "description":serializer.data['description'],
            "category":serializer.data['category'],
            "expense_date":serializer.data['expense_date'],
            "currency": currency
        }
        return Response(data=result, status=status.HTTP_200_OK)
