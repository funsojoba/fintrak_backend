from rest_framework.views import APIView
from income_app.models import Income
from income_app.serializers.income_serializer import IncomeSerializer
from rest_framework import permissions, status
from lib.response import Response

class ListIncomeView(APIView):
    serializer_class = IncomeSerializer
    permission_classes = [permissions.IsAuthenticated]
   
    def get(self, request):
        owner = request.user

        income_query = Income.objects.filter(owner=owner)
        serializer = self.serializer_class(income_query, many=True)
        data = serializer.data
        count = income_query.count()

        return Response(data={"data":data, "count":count}, status=status.HTTP_200_OK)