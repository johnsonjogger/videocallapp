# Generated by Django 2.2.7 on 2021-12-30 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20211229_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lizzyprofile',
            name='id_token',
            field=models.CharField(blank=True, max_length=1000, unique=True),
        ),
        migrations.AlterField(
            model_name='nadiaprofile',
            name='id_token',
            field=models.CharField(blank=True, max_length=1000, unique=True),
        ),
    ]
