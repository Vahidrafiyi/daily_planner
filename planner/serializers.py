from django.contrib.auth.models import User
from rest_framework import serializers

from planner.models import DailyPlanner, Task, SubTask

class TodayGoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyPlanner
        fields = ['id','today_goal', 'date', 'done']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class DailyPlannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyPlanner
        exclude = ['today_goal', 'user']

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        exclude =['user']


# class BeverageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = DailyPlanner
#         fields = ('user', 'drink')

class SubTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubTask
        fields = '__all__'