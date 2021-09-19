from rest_framework.views import APIView
from rest_framework import permissions, status

from lib.response import Response
from expense_app.models import Expense


class DeleteExpenseView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, pk):
        expense = Expense.objects.get(id=pk)
        expense.delete()
        return Response(data={"message": "Expense deleted"}, status=status.HTTP_204_NO_CONTENT)
