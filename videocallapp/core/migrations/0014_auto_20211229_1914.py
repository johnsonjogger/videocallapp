# Generated by Django 2.2.7 on 2021-12-29 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20211229_1814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lizzyprofile',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='nadiaprofile',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
