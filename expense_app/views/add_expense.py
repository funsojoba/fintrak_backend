from expense_app.models import Expense

from rest_framework import views, permissions, status

from lib.response import Response
from expense_app.serializers.expense_serializer import ExpenseSerializer


class AddExpenseView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ExpenseSerializer

    def post(self, request):
        owner = request.user
        data = request.data
        seriailzer = self.serializer_class(data=data)

        seriailzer.is_valid(raise_exception=True)

        amount = data.get('amount', '')
        category = data.get('category', '')
        description = data.get('description', '')
        expense_date = data.get('expense_date', '')

        income = Expense.objects.create(owner = owner, amount=amount, category=category, description=description, expense_date=expense_date)

        return Response(data={"message":"success"}, status=status.HTTP_201_CREATED)
