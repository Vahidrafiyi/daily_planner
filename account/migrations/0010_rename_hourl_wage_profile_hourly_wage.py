# Generated by Django 3.2.7 on 2022-03-01 08:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_alter_salaryreceipt_total_hours'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='hourl_wage',
            new_name='hourly_wage',
        ),
    ]
