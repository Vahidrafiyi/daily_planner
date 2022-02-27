from django.contrib.auth.models import User
from rest_framework import serializers

from eventlog.models import EnterExit


class EnterExitSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnterExit
        fields = '__all__'