from datetime import datetime
from django.db.models import Sum

from rest_framework.views import APIView
from rest_framework import permissions, status

from income_app.models import Income
from income_app.serializers.income_serializer import IncomeSerializer
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

        # income per month
        current_month = datetime.now().month
        income_per_month = Income.objects.filter(owner=owner, income_date__month=current_month)
        current_month_serializer = self.serializer_class(income_per_month, many=True)

        # total income
        total_income = Income.objects.filter(owner=owner, income_date__month=current_month).aggregate(Sum('amount'))
        #sum by source group

        sum_by_sources = Income.objects.filter(owner=owner, income_date__month=current_month).values('source').annotate(source_total=Sum('amount'))

        return Response(data={"data":data, 
                            "count":count, 
                            "income_per_month":current_month_serializer.data, 
                            'total_income':total_income,
                            'income_per_source':sum_by_sources}, status=status.HTTP_200_OK)
