# Generated by Django 3.2.7 on 2022-02-26 07:46

from django.db import migrations
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0003_auto_20220225_2252'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=django_jalali.db.models.jDateField(auto_now=True),
        ),
    ]
