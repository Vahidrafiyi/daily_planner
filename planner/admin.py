from django.contrib import admin
from django.contrib.admin import register

from planner.models import DailyPlanner, Task, SubTask, TodayGoal
from django_jalali.admin.filters import JDateFieldListFilter
import django_jalali.admin as jadmin


@register(DailyPlanner)
class DaillyPlannerAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'what_day')

@register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('task_title', 'time', 'user', 'done')

@register(SubTask)
class SubTaskAdmin(admin.ModelAdmin):
    list_display = ('user', 'subtask_title')

@register(TodayGoal)
class TodayGoalAdmin(admin.ModelAdmin):
    list_display = ('user', 'today_goal', 'date', 'done')
    list_filter = (
        ('date', JDateFieldListFilter),
    )


