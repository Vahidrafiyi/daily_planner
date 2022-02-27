import datetime

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import User
from django_jalali.db import models as jmodels

from jalali_date import date2jalali

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='task')
    task_title = models.CharField(max_length=255)
    time = models.DurationField()
    date = jmodels.jDateField(default='1400-12-07')
    done = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.task_title}'

    def date_to_jalali(self):
        return date2jalali(self.date)


class SubTask(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subtask')
    task = models.ForeignKey(Task, models.CASCADE)
    subtask_title = models.CharField(max_length=255)
    time = models.DurationField()
    date = jmodels.jDateField(default='1400-12-06')
    done = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.subtask_title}'

    def date_to_jalali(self):
        return date2jalali(self.date)

class TodayGoal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    today_goal = models.CharField(max_length=128)
    date = jmodels.jDateField(default='1400-12-07')
    done = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} {self.today_goal}'

    def date_to_jalali(self):
        return date2jalali(self.date)

class DailyPlanner(models.Model):
    # BOSS = 1
    # MANAGER = 2
    # SUPERVISOR = 3
    # STAFF = 4
    # SAT = 1
    # SUN = 2
    # MON = 3
    # TUE = 4
    # WED = 5
    # THU = 6
    # FRI = 7
    ROLES = [
        ('BOSS', 'BOSS'),
        ('MANAGER', 'MANAGER'),
        ('SUPERVISOR', 'SUPERVISOR'),
        ('STAFF', 'STAFF'),
    ]
    WHAT_DAYS = [
        ('SAT', 'SAT'),
        ('SUN', 'SUN'),
        ('MON', 'MON'),
        ('THU', 'TUE'),
        ('WED', 'WED'),
        ('THU', 'THU'),
        ('FRI', 'FRI'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='plan+')
    role = models.CharField(max_length=10, choices=ROLES, default=ROLES[3][0])
    today_goal = models.ForeignKey(TodayGoal, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='plan+', null=True)
    sub_task = models.ForeignKey(SubTask, on_delete=models.CASCADE, related_name='plan+', null=True, blank=True)
    inspiration = models.TextField(blank=True, null=True)
    education_title = models.CharField(max_length=128, blank=True, null=True)
    education_time = models.DurationField(blank=True, null=True)
    breakfast_start_time = models.TimeField(blank=True, null=True)
    breakfast_end_time = models.TimeField(blank=True, null=True)
    lunch_start_time = models.TimeField(blank=True, null=True)
    lunch_end_time = models.TimeField(blank=True, null=True)
    gaming_start_time = models.TimeField(blank=True, null=True)
    gaming_end_time = models.TimeField(blank=True, null=True)
    drink = models.PositiveSmallIntegerField(default=0, validators=(MinValueValidator(0), MaxValueValidator(8)))
    mind_dump = models.TextField(blank=True, null=True)
    date = jmodels.jDateField(default='1400-12-07')
    what_day = models.CharField(max_length=3, choices=WHAT_DAYS, default=WHAT_DAYS[0][0])

    def __str__(self):
        return str(self.user) + ' ' + str(self.today_goal)

    def date_to_jalali(self):
        return date2jalali(self.date)

