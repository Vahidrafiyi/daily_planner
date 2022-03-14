# Generated by Django 3.2.7 on 2022-03-14 10:57

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
            name='DailyPlanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inspiration', models.TextField(blank=True, null=True)),
                ('education_title', models.CharField(blank=True, max_length=128, null=True)),
                ('education_time', models.DurationField(blank=True, null=True)),
                ('breakfast_start_time', models.TimeField(blank=True, null=True)),
                ('breakfast_end_time', models.TimeField(blank=True, null=True)),
                ('lunch_start_time', models.TimeField(blank=True, null=True)),
                ('lunch_end_time', models.TimeField(blank=True, null=True)),
                ('gaming_start_time', models.TimeField(blank=True, null=True)),
                ('gaming_end_time', models.TimeField(blank=True, null=True)),
                ('drink', models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(8)])),
                ('mind_dump', models.TextField(blank=True, null=True)),
                ('date', django_jalali.db.models.jDateField(default='1400-12-07')),
                ('what_day', models.CharField(choices=[('SAT', 'SAT'), ('SUN', 'SUN'), ('MON', 'MON'), ('THU', 'TUE'), ('WED', 'WED'), ('THU', 'THU'), ('FRI', 'FRI')], default='SAT', max_length=3)),
            ],
        ),
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
                ('time', models.DurationField()),
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
                ('time', models.DurationField()),
                ('date', django_jalali.db.models.jDateField(default='1400-12-06')),
                ('done', models.BooleanField(default=False)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='planner.task')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subtask', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('date', django_jalali.db.models.jDateField()),
                ('daily_planner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='planner.dailyplanner')),
                ('feedback_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feedbacker', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feedbackee', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='dailyplanner',
            name='sub_task',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='plan+', to='planner.subtask'),
        ),
        migrations.AddField(
            model_name='dailyplanner',
            name='task',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='plan+', to='planner.task'),
        ),
        migrations.AddField(
            model_name='dailyplanner',
            name='today_goal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='planner.todaygoal'),
        ),
        migrations.AddField(
            model_name='dailyplanner',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plan+', to=settings.AUTH_USER_MODEL),
        ),
    ]
