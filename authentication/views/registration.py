from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status


class RegisterView(APIView):
    def get(self, request):
        return Response({"message":"Success"})