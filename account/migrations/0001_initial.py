# Generated by Django 3.2.7 on 2022-03-14 10:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_jalali.db.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('date', django_jalali.db.models.jDateField()),
                ('expiration', django_jalali.db.models.jDateField()),
                ('level', models.CharField(choices=[('very_important', 'very_important'), ('important', 'important'), ('non_important', 'non_important')], default='important', max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('hourly_wage', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='SignUp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=24, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=16)),
                ('password2', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='SalaryReceipt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_code', models.IntegerField(blank=True, null=True)),
                ('from_date', django_jalali.db.models.jDateField()),
                ('to_date', django_jalali.db.models.jDateField()),
                ('total_hours', models.FloatField(blank=True, null=True)),
                ('salary', models.FloatField(blank=True, null=True)),
                ('hourly_wage', models.IntegerField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_role', models.CharField(choices=[('BOSS', 'BOSS'), ('MANAGER', 'MANAGER'), ('SUPERVISOR', 'SUPERVISOR'), ('STAFF', 'STAFF'), ('TEACHER', 'TEACHER'), ('FREELANCER', 'FREELANCER'), ('ADMIN', 'ADMIN'), ('INTERN', 'INTERN')], default='STAFF', max_length=10)),
                ('second_role', models.CharField(blank=True, choices=[('BOSS', 'BOSS'), ('MANAGER', 'MANAGER'), ('SUPERVISOR', 'SUPERVISOR'), ('STAFF', 'STAFF'), ('TEACHER', 'TEACHER'), ('FREELANCER', 'FREELANCER'), ('ADMIN', 'ADMIN'), ('INTERN', 'INTERN')], default='STAFF', max_length=10, null=True)),
                ('first_name', models.CharField(blank=True, max_length=24, null=True)),
                ('last_name', models.CharField(blank=True, max_length=24, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], default='male', max_length=10)),
                ('employee_code', models.IntegerField(unique=True)),
                ('code_melli', models.IntegerField(blank=True, null=True)),
                ('code_passport', models.IntegerField(blank=True, null=True)),
                ('code_shenasname', models.IntegerField(blank=True, null=True)),
                ('father_name', models.CharField(blank=True, max_length=34, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/images/profile')),
                ('phone', models.IntegerField(blank=True, null=True)),
                ('emergency_phone', models.IntegerField(blank=True, null=True)),
                ('date_joined', django_jalali.db.models.jDateTimeField(blank=True, null=True)),
                ('announcement', models.ManyToManyField(blank=True, to='account.Announcement')),
                ('group', models.ManyToManyField(blank=True, to='account.Group')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permissions', models.CharField(max_length=128)),
                ('is_granted', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
