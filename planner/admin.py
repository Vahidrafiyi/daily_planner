from django.contrib import admin
from django.contrib.admin import register

from planner.models import DailyPlanner, Task, SubTask


@register(DailyPlanner)
class DaillyPlannerAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'what_day', 'role')

@register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('task_title', 'time', 'user', 'done')

@register(SubTask)
class SubTaskAdmin(admin.ModelAdmin):
    list_display = ('user', 'subtask_title')


