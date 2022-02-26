from datetime import datetime

from django.contrib.auth import login
from django.db.models.signals import post_save
from django.utils import timezone

from django.contrib.auth.models import User
from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.dispatch import receiver

from rest_framework.authtoken.views import ObtainAuthToken
from eventlog.models import EnterExit

@receiver(post_save, sender=ObtainAuthToken)
def log_user_login(sender, request, user, **kwargs):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    # print(datetime.datetime.now)
    EnterExit.objects.create(user=request.user,enter_time=timezone.now(), exit_time='')

@receiver(user_logged_out)
def log_user_logout(sender, request, user, **kwargs):
    EnterExit.objects.update(exit_time=timezone.now())