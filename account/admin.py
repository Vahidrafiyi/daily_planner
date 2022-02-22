from django.contrib import admin
from django.contrib.admin import register
from account.models import SignUp,LogIn


@register(SignUp)
class SignUpAdmin(admin.ModelAdmin):
    list_display = ('username', 'email')
