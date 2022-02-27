from django.contrib import admin
from django.contrib.admin import register
from eventlog.models import EnterExit

@register(EnterExit)
class EnterExitAdmin(admin.ModelAdmin):
    list_display = ('user', 'enter_time', 'exit_time', 'date', 'work_time')
