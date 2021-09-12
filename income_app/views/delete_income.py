from rest_framework.views import APIView
from rest_framework import permissions, status

from lib.response import Response
from income_app.models import Income


class DeleteIncomeView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, pk):
        income = Income.objects.get(id=pk)
        income.delete()
        return Response(data={"message": "Income deleted"}, status=status.HTTP_204_NO_CONTENT)
