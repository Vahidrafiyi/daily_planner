from django.db import models
from django.contrib.auth.models import User
from django_jalali.db import models as jmodels

class EnterExit(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='enterexit')
    enter_time = jmodels.jDateTimeField(auto_now=True)
    exit_time = jmodels.jDateTimeField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Enter Exit'

    def __str__(self):
        return str(self.user.username)
