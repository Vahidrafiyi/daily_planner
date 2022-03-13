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


class Group(models.Model):
    title = models.CharField(max_length=50)
    hourly_wage = models.IntegerField()

    def __str__(self):
        return self.title

class Announcement(models.Model):
    LEVEL = (
        ('very_important', 'very_important'),
        ('important', 'important'),
        ('non_important', 'non_important'),
    )
    WHICH_GROUP = (
        ('BOSS', 'BOSS'),
        ('MANAGER', 'MANAGER'),
        ('SUPERVISOR', 'SUPERVISOR'),
        ('STAFF', 'STAFF'),
        ('ADMIN', 'ADMIN'),
        ('TEACHER', 'TEACHER'),
        ('INTERN', 'INTERN'),
        ('FREELANCER', 'FREELANCER'),
        ('ALL', 'ALL'),
        ('WEB', 'WEB'),
        ('GRAPHIC', 'GRAPHIC'),
        ('CONTENT_PRODUCTION', 'CONTENT_PRODUCTION'),
    )
    title = models.CharField(max_length=255)
    body = models.TextField()
    date = jmodels.jDateTimeField()
    expiration = jmodels.jDateTimeField()
    which_group = models.CharField(max_length=18, choices=WHICH_GROUP, default=WHICH_GROUP[8][0])
    level = models.CharField(max_length=32, choices=LEVEL, default=LEVEL[1][0])

    def __str__(self):
        return self.title

    def date_to_jalali(self):
        return datetime2jalali(self.date)

    def expiration_to_jalali(self):
        return datetime2jalali(self.expiration)


class Profile(models.Model):
    class Gender(models.TextChoices):
        MALE = 'male'
        FEMALE = 'female'

    ROLES = [
        ('BOSS', 'BOSS'),
        ('MANAGER', 'MANAGER'),
        ('SUPERVISOR', 'SUPERVISOR'),
        ('STAFF', 'STAFF'),
        ('TEACHER', 'TEACHER'),
        ('FREELANCER', 'FREELANCER'),
        ('ADMIN', 'ADMIN'),
        ('INTERN', 'INTERN'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    role = models.CharField(max_length=10, choices=ROLES, default=ROLES[3][0])
    group = models.ManyToManyField(Group, blank=True)
    announcement = models.ManyToManyField(Announcement)
    # notification_body = models.ManyToManyField(Notification, through_fields='body')
    first_name = models.CharField(max_length=24, null=True, blank=True)
    last_name = models.CharField(max_length=24, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=Gender.choices, default=Gender.MALE)
    employee_code = models.IntegerField(unique=True)
    code_melli = models.IntegerField(null=True, blank=True)
    code_passport = models.IntegerField(null=True, blank=True)
    code_shenasname = models.IntegerField(null=True, blank=True)
    father_name = models.CharField(max_length=34, null=True, blank=True)
    image = models.ImageField(upload_to='media/images/profile', null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    emergency_phone = models.IntegerField(null=True, blank=True)
    date_joined = jmodels.jDateTimeField(null=True, blank=True)

    def __str__(self):
        return self.user.username

    def datetime_to_jalali(self):
        return datetime2jalali(self.date_joined)

class SalaryReceipt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    employee_code = models.IntegerField(null=True, blank=True)
    from_date = jmodels.jDateField()
    to_date = jmodels.jDateField()
    total_hours = models.FloatField(null=True, blank=True)
    salary = models.FloatField(null=True, blank=True)
    hourly_wage = models.IntegerField(null=True, blank=True)

    def from_date_to_jalali(self):
        return date2jalali(self.to_date)

    def to_date_to_jalali(self):
        return date2jalali(self.to_date)

    def __str__(self):
        return f'salary receipt for {self.user.username} at date: {self.to_date}'


class Permission(models.Model):
    permissions = models.CharField(max_length=128)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_granted = models.BooleanField(default=False)