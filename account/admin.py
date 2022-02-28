from django.contrib import admin
from django.contrib.admin import register
from account.models import SignUp, LogIn, Profile


@register(SignUp)
class SignUpAdmin(admin.ModelAdmin):
    list_display = ('username', 'email')

@register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user','employee_code', 'phone' )
