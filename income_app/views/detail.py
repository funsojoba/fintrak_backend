from rest_framework.views import APIView
from rest_framework import permissions, status

from lib.response import Response
from income_app.models import Income
from income_app.serializers.income_serializer import IncomeSerializer

from user_app.models import UserProfile

class IncomeDetial(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = IncomeSerializer

    def get(self, request, pk):
        income = Income.objects.get(id=pk)
        serializer = self.serializer_class(income)
        print(request.user)

        user_profile = UserProfile.objects.filter(user=request.user)
        currency = user_profile.currency if user_profile else '$'

        result = {
            "data": serializer.data,
            "currency": currency
        }
        return Response(data=result, status=status.HTTP_200_OK)
