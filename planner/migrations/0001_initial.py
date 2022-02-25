# Generated by Django 3.2.7 on 2022-02-24 12:26

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
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_title', models.CharField(max_length=255)),
                ('time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='EnterExit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enter_time', models.TimeField()),
                ('exit_time', models.TimeField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='enterexit', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Enter Exit',
            },
        ),
        migrations.CreateModel(
            name='DailyPlanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.PositiveSmallIntegerField(choices=[(1, 'BOSS'), (2, 'MANAGER'), (3, 'SUPERVISOR'), (4, 'STAFF')], default=4)),
                ('today_goal', models.TextField()),
                ('inspiration', models.TextField(blank=True, null=True)),
                ('education_title', models.CharField(blank=True, max_length=128, null=True)),
                ('education_time', models.TimeField(blank=True, null=True)),
                ('breakfast_time', models.TimeField(blank=True, null=True)),
                ('lunch_time', models.TimeField(blank=True, null=True)),
                ('gaming_time', models.TimeField(blank=True, null=True)),
                ('drink', models.PositiveSmallIntegerField(default=0)),
                ('mind_dump', models.TextField(blank=True, null=True)),
                ('date', django_jalali.db.models.jDateField(auto_now=True)),
                ('what_day', models.PositiveSmallIntegerField(choices=[(1, 'SAT'), (2, 'SUN'), (3, 'MON'), (6, 'TUE'), (5, 'WED'), (6, 'THU'), (7, 'FRI')], default=1)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='plan', to='planner.task')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plan', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
