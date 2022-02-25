from django.contrib.auth.models import User
from rest_framework import serializers

from planner.models import DailyPlanner, Task, EnterExit

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class DailyPlannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyPlanner
        fields = '__all__'
        depth = 1

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class EnterExitSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnterExit
        fields = '__all__'

# class BeverageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = DailyPlanner
#         fields = ('user', 'drink')

