# Generated by Django 3.2.7 on 2022-03-13 11:28

from django.db import migrations
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0036_auto_20220313_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='date',
            field=django_jalali.db.models.jDateTimeField(),
        ),
    ]