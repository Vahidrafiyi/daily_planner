from django.db import models
from django.contrib.auth.models import User
from django_jalali.db import models as jmodels
from jalali_date import date2jalali


class EnterExit(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='enterexit')
    enter_time = jmodels.jDateTimeField(blank=True, null=True)
    exit_time = jmodels.jDateTimeField(blank=True, null=True)
    work_time = models.DurationField(default=None, blank=True, null=True)
    date = jmodels.jDateField(default='1400-12-07')
    is_paid = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Enter Exit'

    def __str__(self):
        return str(self.user.username)

    def date_to_jalali(self):
        return date2jalali(self.date)
