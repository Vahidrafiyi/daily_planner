from django.contrib import admin
from django.contrib.admin import register
from eventlog.models import EnterExit

@register(EnterExit)
class EnterExitAdmin(admin.ModelAdmin):
    list_display = ('user','date', 'work_time', 'is_paid')
    list_editable = ('is_paid',)
