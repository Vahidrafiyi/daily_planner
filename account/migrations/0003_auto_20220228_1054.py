# Generated by Django 3.2.7 on 2022-02-28 07:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='code_melli',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(10), django.core.validators.MaxValueValidator(10)]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='code_shenasname',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]