# Generated by Django 3.2.7 on 2022-03-07 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventlog', '0004_enterexit_is_paid'),
    ]

    operations = [
        migrations.AddField(
            model_name='enterexit',
            name='done_percent_goal',
            field=models.PositiveSmallIntegerField(default=1),
            preserve_default=False,
        ),
    ]
