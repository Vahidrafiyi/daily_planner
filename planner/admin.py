from django.contrib import admin
from django.contrib.admin import register

from planner.models import DailyPlanner, EnterExit, Task

@register(DailyPlanner)
class DaillyPlannerAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'what_day', 'role')

@register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('task_title', 'time')
