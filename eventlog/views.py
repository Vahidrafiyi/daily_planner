import datetime

from django.shortcuts import render
from django.utils import timezone
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from eventlog.models import EnterExit
from eventlog.serializers import EnterExitSerializer, EnterSerializer


class EnterExitAPI(APIView):
    def get(self, request):
        query = EnterExit.objects.all()
        serializer = EnterExitSerializer(query)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)

    # def post(self, request):
    #     serializer = EnterSerializer(data=request.data)
    #     data = {}
    #     if serializer.is_valid():
    #         data['user'] = request.user.id
    #         data['enter_time'] = timezone.now()
    #         data['role'] = request.data.get('role')
    #         serializer.save()
    #         return Response(data, status=201)
    #     data['error'] = 'something went wrong...'
    #     return Response(serializer.errors, status=400)

class EnterExitAllAPI(APIView):
    permission_classes = (AllowAny,)
    def get(self, request):
        queryset = EnterExit.objects.all()
        serializer = EnterExitSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
