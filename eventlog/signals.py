import datetime
from django.db.models.signals import post_save, post_delete

from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from eventlog.models import EnterExit
from planner.models import TodayGoal


@receiver(post_save, sender=Token)
def log_user_login(sender, instance, created, **kwargs):
    if created:
        EnterExit.objects.create(user=instance.user, enter_time=datetime.datetime.now(), date=datetime.date.today(), exit_time='', work_time=None)

@receiver(post_delete, sender=Token)
def log_user_logout(sender, instance, **kwargs):
        todaygoal_done = TodayGoal.objects.filter(user=instance.user, date=datetime.date.today(), done=True).count()
        todaygoal_count = TodayGoal.objects.filter(user=instance.user, date=datetime.date.today()).count()
        todaygoal = int((todaygoal_done / todaygoal_count) * 100)
        print(todaygoal)
        query = EnterExit.objects.filter(user=instance.user, date=datetime.date.today())
        query.update(exit_time=datetime.datetime.now())
        print(query)
        work_time = query[0].exit_time - query[0].enter_time
        query.update(work_time=work_time, done_percent_goal=todaygoal)
