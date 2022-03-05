# Generated by Django 3.2.7 on 2022-02-27 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0002_alter_task_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dailyplanner',
            old_name='breakfast_time',
            new_name='breakfast_end_time',
        ),
        migrations.RenameField(
            model_name='dailyplanner',
            old_name='gaming_time',
            new_name='breakfast_start_time',
        ),
        migrations.RenameField(
            model_name='dailyplanner',
            old_name='lunch_time',
            new_name='gaming_end_time',
        ),
        migrations.AddField(
            model_name='dailyplanner',
            name='gaming_start_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='dailyplanner',
            name='lunch_end_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='dailyplanner',
            name='lunch_start_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dailyplanner',
            name='education_time',
            field=models.DurationField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='subtask',
            name='time',
            field=models.DurationField(),
        ),
    ]
