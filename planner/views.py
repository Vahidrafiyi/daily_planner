from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken

from planner.models import DailyPlanner, Task, EnterExit
from planner.serializers import DailyPlannerSerializer, TaskSerializer, EnterExitSerializer

class DailyPlannerAPI(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    def get(self, request, username):
        queryset = DailyPlanner.objects.filter(user__username=username)
        serializer = DailyPlannerSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    # def post(self, request):
    #     serializer = DailyPlannerSerializer(data=request.data)
    #     print(request.data)
    #     if serializer.is_valid():
    #         DailyPlanner.user.username = request.user.username
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
