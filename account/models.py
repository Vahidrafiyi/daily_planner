from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import User

from django_jalali.db import models as jmodels
from jalali_date import datetime2jalali, date2jalali


class SignUp(models.Model):
    username = models.CharField(max_length=24, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=16)
    password2 = models.CharField(max_length=16)

    def __str__(self):
        return f'{self.username} signed up'

class LogIn(models.Model):
    username = models.CharField(max_length=24)
    password = models.CharField(max_length=16)
    
    def __str__(self):
        return f'{self.username} loged in'

class Profile(models.Model):
    class Gender(models.TextChoices):
        MALE = 'male'
        FEMALE = 'female'

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    gender = models.CharField(max_length=10, choices=Gender.choices, default=Gender.MALE)
    employee_code = models.IntegerField(unique=True)
    code_melli = models.IntegerField(null=True, blank=True)
    code_passport = models.IntegerField(null=True, blank=True)
    code_shenasname = models.IntegerField(null=True, blank=True)
    father_name = models.CharField(max_length=34, null=True, blank=True)
    image = models.ImageField(upload_to='media/images/profile', null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    emergency_phone = models.IntegerField(null=True, blank=True)
    hourly_wage = models.IntegerField(null=True, blank=True)
    date_joined = jmodels.jDateTimeField()

    def __str__(self):
        return self.user.username

    def datetime_to_jalali(self):
        return datetime2jalali(self.date_joined)

class SalaryReceipt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    employee_code = models.IntegerField()
    payment_date = jmodels.jDateField()
    total_hours = models.FloatField()
    salary = models.FloatField()

    def date_to_jalali(self):
        return date2jalali(self.payment_date)
