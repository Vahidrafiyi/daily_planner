import datetime

from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from planner.models import DailyPlanner, Task, SubTask, TodayGoal
from planner.serializers import DailyPlannerSerializer, TaskSerializer, UserSerializer, \
    SubTaskSerializer, TodayGoalSerializer


# TODAY GOALS API
class ShowTodayGoalAPI(APIView):
    def get(self, request):
        queryset = TodayGoal.objects.filter(user=request.user, done=False)
        serializer = TodayGoalSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class EnterTodayGoalAPI(APIView):
    def post(self, request):
        serializer = TodayGoalSerializer(data=request.data)
        count = TodayGoal.objects.filter(date=datetime.date.today()).count()
        if serializer.is_valid():
            data = {}
            serializer.validated_data['user'] = request.user
            print(serializer.validated_data)
            print(request.user)
            if request.user.is_staff == True:
                data['role limitation'] = 'the staff can not specify today goal.'
                return Response(data, status=status.HTTP_401_UNAUTHORIZED)
            if count >= 3 :
                data['number limit'] = 'You can not set more than 3 goals per day'
                return Response(data, status=status.HTTP_401_UNAUTHORIZED)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request):
        query = TodayGoal.objects.get(user=request.user, date=datetime.date.today())
        serializer = TodayGoalSerializer(query, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EnterDoneGoalAPI(APIView):
    def patch(self, request, pk):
        query = TodayGoal.objects.get(user_id=pk, date=datetime.date.today())
        serializer = TodayGoalSerializer(query, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ShowTodayGoalPercentAPI(APIView):
    def get(self, request, pk):
        todaygoal_done = TodayGoal.objects.filter(user_id=pk,date=datetime.date.today(),done=True)
        todaygoal_count = TodayGoal.objects.filter(user_id=pk,date=datetime.date.today()).count()
        todaygoal = todaygoal_done / todaygoal_count
        todaygoal_percent = format(todaygoal, '.2%')
        serializer = TodayGoalSerializer(todaygoal_percent, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# DAILY PLAN API
class EnterPlan(APIView):
    def post(self, request):
        serializer = DailyPlannerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['user'] = request.user
            serializer.validated_data['date'] = datetime.date.today()
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AllPlan(APIView):
    def get(self, request):
        queryset = DailyPlanner.objects.filter(user=request.user)
        serializer = DailyPlannerSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request):
        query = DailyPlanner.objects.get(user=request.user, date=datetime.date.today())
        serializer = DailyPlannerSerializer(query, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserAPI(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# TASK API
class EnterTaskAPI(APIView):
    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        objects_number = Task.objects.filter(user=request.user, date=datetime.date.today()).count()
        print(request.user)
        # print(serializer.validated_data['user'])
        print(request.user.id)
        if serializer.is_valid():
            serializer.validated_data['user'] = request.user
            if objects_number >= 5:
                data = {'task limitation':'you can have only 5 tasks per day'}
                return Response(status=status.HTTP_401_UNAUTHORIZED, data=data)
            else:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskAPI(APIView):
    def get(self, request):
        print(request.user)
        queryset = Task.objects.filter(date=datetime.date.today(), user=request.user)
        serializer = TaskSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request):
        query = Task.objects.get(user=request.user)
        serializer = TaskSerializer(query, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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

# SUB_TASK API
class EnterSubTaskAPI(APIView):
    def post(self, request):
        serializer = SubTaskSerializer(data=request.data)
        objects_number = SubTask.objects.filter(user=request.user, date=datetime.date.today()).count()
        if serializer.is_valid():
            if objects_number >= 7:
                data = {'sub_task limitation':'you can have only 7 tasks per day'}
                return Response(status=status.HTTP_401_UNAUTHORIZED, data=data)
            else:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SubTaskAPI(APIView):
    def get(self, request):
        queryset = SubTask.objects.filter(user=request.user)
        serializer = SubTaskSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request):
        query = SubTask.objects.get(user=request.user)
        serializer = SubTaskSerializer(query, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DrinkAPI(APIView):
    def get(self, request):
        query = DailyPlanner.objects.filter(user=request.user, date=datetime.date.today())
        # print(query)
        if query[0].drink < 8:
            # print(query[0].drink)
            query.update(drink=query[0].drink + 1)
            serializer = DailyPlannerSerializer(query, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        data = {'drink limitation': 'you can not add more than 8 glass per day'}
        return Response(data, status=status.HTTP_401_UNAUTHORIZED)

    # def get(self, request):
    #     query = DailyPlanner.objects.filter(user=request.user, date=datetime.date.today())
    #     serializer = DailyPlannerSerializer(query, data=request.data)
    #     if serializer.is_valid():
    #         query.update(drink=query[0].drink+1)
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
