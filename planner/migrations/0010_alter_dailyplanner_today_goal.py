# Generated by Django 3.2.7 on 2022-02-26 11:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0009_alter_task_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailyplanner',
            name='today_goal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='planner.todaygoal'),
        ),
    ]
