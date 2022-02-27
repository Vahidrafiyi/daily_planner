# Generated by Django 3.2.7 on 2022-02-27 07:39

from django.conf import settings
import django.core.validators
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
            name='TodayGoal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('today_goal', models.CharField(max_length=128)),
                ('date', django_jalali.db.models.jDateField(default='1400-12-07')),
                ('done', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_title', models.CharField(max_length=255)),
                ('time', models.TimeField()),
                ('date', django_jalali.db.models.jDateField(default='1400-12-07')),
                ('done', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='task', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SubTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subtask_title', models.CharField(max_length=255)),
                ('time', models.TimeField()),
                ('date', django_jalali.db.models.jDateField(default='1400-12-06')),
                ('done', models.BooleanField(default=False)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='planner.task')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subtask', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DailyPlanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('BOSS', 'BOSS'), ('MANAGER', 'MANAGER'), ('SUPERVISOR', 'SUPERVISOR'), ('STAFF', 'STAFF')], default='STAFF', max_length=10)),
                ('inspiration', models.TextField(blank=True, null=True)),
                ('education_title', models.CharField(blank=True, max_length=128, null=True)),
                ('education_time', models.TimeField(blank=True, null=True)),
                ('breakfast_time', models.TimeField(blank=True, null=True)),
                ('lunch_time', models.TimeField(blank=True, null=True)),
                ('gaming_time', models.TimeField(blank=True, null=True)),
                ('drink', models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(8)])),
                ('mind_dump', models.TextField(blank=True, null=True)),
                ('date', django_jalali.db.models.jDateField(default='1400-12-07')),
                ('what_day', models.CharField(choices=[('SAT', 'SAT'), ('SUN', 'SUN'), ('MON', 'MON'), ('THU', 'TUE'), ('WED', 'WED'), ('THU', 'THU'), ('FRI', 'FRI')], default='SAT', max_length=3)),
                ('sub_task', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='plan+', to='planner.subtask')),
                ('task', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='plan+', to='planner.task')),
                ('today_goal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='planner.todaygoal')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plan+', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
