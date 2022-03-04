from rest_framework.views import APIView
from rest_framework import permissions, status

from lib.response import Response
from income_app.models import Income
from income_app.serializers.income_serializer import IncomeSerializer


class EditIncomeView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = IncomeSerializer

    def patch(self, request, pk):
        income = Income.objects.get(id=pk)
        serializer = self.serializer_class(income, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(data={"message": "success"}, status=status.HTTP_200_OK)
        return Response(errors={"message":"wrong parameters"}, status=status.HTTP_400_BAD_REQUEST)
