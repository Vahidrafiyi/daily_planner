# Generated by Django 3.2.7 on 2022-03-09 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0028_auto_20220309_1104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salaryreceipt',
            name='hourly_wage',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]