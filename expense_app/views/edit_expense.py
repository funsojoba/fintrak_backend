from rest_framework import views, permissions, status

from expense_app.models import Expense
from lib.response import Response

from expense_app.serializers.expense_serializer import ExpenseSerializer


class EditExpenseView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ExpenseSerializer

    def put(self, request, pk, format=None):
        expense = Expense.objects.get(id=pk)
        serializer = self.serializer_class(expense)

        data = request.data

        amount = data.get('amount', '')
        category = data.get('category', '')
        description = data.get('description', '')
        expense_date = data.get('income_date', '')

        if not amount:
            amount = expense.amount

        if not category:
            category = expense.category

        if not description:
            description = expense.description

        if not expense_date:
            expense_date = expense.expense_date

        expense.amount = amount
        expense.category = category
        expense.description = description
        expense.expense_date = expense_date
        expense.save()
        return Response(data={"message": "success"}, status=status.HTTP_200_OK)
