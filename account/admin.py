from django.contrib import admin
from django.contrib.admin import register
from account.models import Profile, SalaryReceipt, Permission, Group, Announcement


@register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user','employee_code', 'phone', 'id' )

@register(SalaryReceipt)
class SalaryReceiptAdmin(admin.ModelAdmin):
    list_display = ('user','employee_code', 'to_date', 'salary' )

@register(Permission)
class PermissionAdmin(admin.ModelAdmin):
    list_display = ('user','permissions', 'is_granted')

@register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('title', 'hourly_wage')

@register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'which_group')
