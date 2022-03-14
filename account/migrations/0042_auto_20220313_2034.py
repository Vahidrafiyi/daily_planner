# Generated by Django 3.2.7 on 2022-03-13 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0041_alter_profile_group'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='role',
        ),
        migrations.AlterField(
            model_name='profile',
            name='group',
            field=models.ManyToManyField(blank=True, to='account.Group'),
        ),
    ]
