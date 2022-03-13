# Generated by Django 3.2.7 on 2022-03-07 10:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0022_auto_20220303_1915'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('user', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('date', django_jalali.db.models.jDateField()),
                ('expiration', django_jalali.db.models.jDateField()),
                ('level', models.CharField(choices=[('very_important', 'very_important'), ('important', 'important'), ('non_important', 'non_important')], default='important', max_length=32)),
                ('seen', models.BooleanField(default=False)),
                ('which_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.group')),
            ],
        ),
        migrations.CreateModel(
            name='WorkLeave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', django_jalali.db.models.jDateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='LogIn',
        ),
        migrations.AddField(
            model_name='profile',
            name='role',
            field=models.CharField(choices=[('BOSS', 'BOSS'), ('MANAGER', 'MANAGER'), ('SUPERVISOR', 'SUPERVISOR'), ('STAFF', 'STAFF'), ('TEACHER', 'TEACHER'), ('FREELANCER', 'FREELANCER')], default='STAFF', max_length=10),
        ),
    ]
