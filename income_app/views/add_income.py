from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.response import Response


class AddIncomeView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        pass