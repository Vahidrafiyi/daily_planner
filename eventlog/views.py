from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from eventlog.models import EnterExit
from eventlog.serializers import EnterExitSerializer


class EnterExitAPI(APIView):
    def get(self, request):
        queryset = EnterExit.objects.filter(user=request.user)
        serializer = EnterExitSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
