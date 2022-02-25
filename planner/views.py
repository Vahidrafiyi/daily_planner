from django.contrib.auth.models import User
from rest_framework import status, mixins
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListCreateAPIView, ListAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication, BasicAuthentication, SessionAuthentication
from rest_framework.authtoken.views import ObtainAuthToken

from planner.models import DailyPlanner, Task, EnterExit
from planner.serializers import DailyPlannerSerializer, TaskSerializer, EnterExitSerializer, UserSerializer


class AllPlan(APIView):
    def get(self, request, username):
        queryset = DailyPlanner.objects.filter(user__username=username)
        serializer = DailyPlannerSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = DailyPlannerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, username):
        query = DailyPlanner.objects.get(user__username=username)
        serializer = DailyPlannerSerializer(query, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskAPI(ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class UserAPI(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# class BeverageCreate(CreateAPIView, mixins.DestroyModelMixin):
#     serializer_class = BeverageSerializer
#     permission_classes = [IsAuthenticatedOrReadOnly]
#
#     def get_queryset(self):
#         user = self.request.user
#         beverage = self.request.data['drink']
#         return DailyPlanner.objects.filter(user=user, drink__exact=beverage)
#
#     def perform_create(self, serializer):
#         if self.get_queryset().exists():
#             raise ValidationError ('you have already voted for this post :)')
#         serializer.save(user=self.request.user, drink__exact=self.request.data['drink'])
