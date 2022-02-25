from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import User
from django_jalali.db import models as jmodels

class Task(models.Model):
    task_title = models.CharField(max_length=255)
    time = models.TimeField()
    done = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.task_title}'

class SubTask(models.Model):
    task = models.ForeignKey(Task, models.CASCADE)
    task_title = models.CharField(max_length=255)
    time = models.TimeField()
    done = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.task_title}'

class DailyPlanner(models.Model):
    BOSS = 1
    MANAGER = 2
    SUPERVISOR = 3
    STAFF = 4
    SAT = 1
    SUN = 2
    MON = 3
    TUE = 4
    WED = 5
    THU = 6
    FRI = 7
    ROLES = [
        (BOSS, 'BOSS'),
        (MANAGER, 'MANAGER'),
        (SUPERVISOR, 'SUPERVISOR'),
        (STAFF, 'STAFF'),
    ]
    WHAT_DAYS = [
        (SAT, 'SAT'),
        (SUN, 'SUN'),
        (MON, 'MON'),
        (THU, 'TUE'),
        (WED, 'WED'),
        (THU, 'THU'),
        (FRI, 'FRI'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='plan', null=True)
    role = models.PositiveSmallIntegerField(choices=ROLES, default=STAFF)
    today_goal = models.TextField()
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='plan', null=True)
    sub_task = models.ForeignKey(SubTask, on_delete=models.CASCADE, related_name='plan', null=True, blank=True)
    inspiration = models.TextField(blank=True, null=True)
    education_title = models.CharField(max_length=128, blank=True, null=True)
    education_time = models.TimeField(blank=True, null=True)
    breakfast_time = models.TimeField(blank=True, null=True)
    lunch_time = models.TimeField(blank=True, null=True)
    gaming_time = models.TimeField(blank=True, null=True)
    drink = models.PositiveSmallIntegerField(default=0, validators=(MinValueValidator(0), MaxValueValidator(8)))
    mind_dump = models.TextField(blank=True, null=True)
    date = jmodels.jDateField(auto_now=True)
    what_day = models.PositiveSmallIntegerField(choices=WHAT_DAYS, default=SAT)

    def __str__(self):
        return str(self.user) + ' ' + str(self.today_goal)
class EnterExit(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='enterexit')
    enter_time = models.TimeField()
    exit_time = models.TimeField()

    class Meta:
        verbose_name_plural = 'Enter Exit'

    def __str__(self):
        return str(self.user.username)
