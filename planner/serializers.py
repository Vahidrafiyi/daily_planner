from django.contrib.auth.models import User
from rest_framework import serializers
from django_jalali.serializers.serializerfield import JDateField, JDateTimeField
from planner.models import DailyPlanner, Task, SubTask, TodayGoal


class TodayGoalSerializer(serializers.ModelSerializer):
    date = JDateField()
    class Meta:
        model = TodayGoal
        fields = ['id', 'today_goal', 'date', 'done']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class DailyPlannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyPlanner
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    date = JDateField()
    class Meta:
        model = Task
        exclude =['user']


# class BeverageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = DailyPlanner
#         fields = ('user', 'drink')

class SubTaskSerializer(serializers.ModelSerializer):
    date = JDateField()
    class Meta:
        model = SubTask
        fields = '__all__'