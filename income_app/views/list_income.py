from datetime import datetime
from django.db.models import Sum

from rest_framework.views import APIView
from rest_framework import permissions, status

from user_app.models import UserProfile
from income_app.models import Income
from income_app.serializers.income_serializer import IncomeSerializer
from lib.response import Response

class ListIncomeView(APIView):
    serializer_class = IncomeSerializer
    permission_classes = [permissions.IsAuthenticated]
   
    def get(self, request, month_id):
        owner = request.user

        user_info = UserProfile.objects.filter(user=request.user).first()
        currnency = user_info.prefered_currency if user_info else "$"
        # income per month
        
        income = Income.objects.filter(owner=owner)
        income_per_month = income.filter(owner=owner, income_date__month=month_id).order_by('-income_date')
        current_month_serializer = self.serializer_class(income_per_month, many=True)

        # total income
        total_income = income.filter(owner=owner, income_date__month=month_id).aggregate(Sum('amount'))
        #sum by source group

        sum_by_sources = income.filter(owner=owner, income_date__month=month_id).values('source').annotate(source_total=Sum('amount'))

        return Response(data={ 
                            "currency":currnency,
                            "income_per_month":current_month_serializer.data, 
                            'total_income':total_income['amount__sum'] if total_income['amount__sum'] else 0,
                            'income_per_source':sum_by_sources}, status=status.HTTP_200_OK)
