# Generated by Django 3.2.7 on 2022-03-03 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0018_auto_20220302_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='employee_code',
            field=models.IntegerField(unique=True),
        ),
    ]
