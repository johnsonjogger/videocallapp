# Generated by Django 2.2.7 on 2022-01-30 09:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0027_auto_20220130_0838'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gratjeenprofile',
            name='user',
        ),
        migrations.RemoveField(
            model_name='gratjeenprofile',
            name='user_info',
        ),
        migrations.RemoveField(
            model_name='lizzyprofile',
            name='user',
        ),
        migrations.RemoveField(
            model_name='lizzyprofile',
            name='user_info',
        ),
        migrations.RemoveField(
            model_name='nadiaprofile',
            name='user',
        ),
        migrations.RemoveField(
            model_name='nadiaprofile',
            name='user_info',
        ),
    ]