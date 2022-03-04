from rest_framework import views, permissions, status

from expense_app.models import Expense
from lib.response import Response

from expense_app.serializers.expense_serializer import ExpenseSerializer


class EditExpenseView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ExpenseSerializer

    def patch(self, request, pk, format=None):
        expense = Expense.objects.get(id=pk)
        serializer = self.serializer_class(expense, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data={"message": "success"}, status=status.HTTP_200_OK)
            
        return Response(errors={"message": "Failure"}, status=status.HTTP_400_BAD_REQUEST)
