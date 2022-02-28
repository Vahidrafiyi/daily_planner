import datetime

from django.contrib.auth import login
from django.db.models import F
from django.db.models.signals import post_save, post_delete
from django.utils import timezone

from django.contrib.auth.models import User
from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from rest_framework.authtoken.views import ObtainAuthToken
from eventlog.models import EnterExit

@receiver(post_save, sender=Token)
def log_user_login(sender, instance, created, **kwargs):
    if created:
        EnterExit.objects.create(user=instance.user, enter_time=datetime.datetime.now(), date=datetime.date.today(), exit_time='', work_time=None)

@receiver(post_delete, sender = Token)
def log_user_logout(sender, instance, **kwargs):
        def get_sender(instance):
            return sender.objects.get(user=instance.user)
        get_sender(instance=instance)
        query = EnterExit.objects.filter(user=instance.user, date=datetime.date.today())
        print(query)
        # print(query.enter_time)
        query.update(exit_time=datetime.datetime.now())
        # print(query)
        work_time = query[0].exit_time - query[0].enter_time
        query.update(work_time=work_time)
