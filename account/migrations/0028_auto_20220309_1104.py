# Generated by Django 3.2.7 on 2022-03-09 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0027_auto_20220309_1059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='employee_code',
            field=models.IntegerField(unique=True),
        ),
        migrations.RemoveField(
            model_name='profile',
            name='group',
        ),
        migrations.AddField(
            model_name='profile',
            name='group',
            field=models.ManyToManyField(to='account.Group'),
        ),
    ]
