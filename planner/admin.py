from django.contrib import admin
from django.contrib.admin import register

from planner.models import DailyPlanner, EnterExit, Task

@register(DailyPlanner)
class DaillyPlannerAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'what_day', 'role')

@register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('task_title', 'time')
    def has_add_permission(self, request):
        num_objects = Task.objects.count()
        if num_objects >= 5:
            return False
        else:
            return True

@register(EnterExit)
class EnterExitAdmin(admin.ModelAdmin):
    list_display = ('user', 'enter_time', 'exit_time')

