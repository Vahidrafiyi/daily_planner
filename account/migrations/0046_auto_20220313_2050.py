# Generated by Django 3.2.7 on 2022-03-13 17:20

from django.db import migrations
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0045_auto_20220313_2041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='date',
            field=django_jalali.db.models.jDateField(),
        ),
        migrations.AlterField(
            model_name='announcement',
            name='expiration',
            field=django_jalali.db.models.jDateField(),
        ),
    ]
