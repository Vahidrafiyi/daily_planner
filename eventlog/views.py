from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from eventlog.models import EnterExit
from eventlog.serializers import EnterExitSerializer


class EnterExitAPI(APIView):
    def get(self, request, pk):
        query = EnterExit.objects.filter(user_id=pk)
        serializer = EnterExitSerializer(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class EnterExitAllAPI(APIView):
    permission_classes = (AllowAny,)
    def get(self, request):
        queryset = EnterExit.objects.all()
        serializer = EnterExitSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
