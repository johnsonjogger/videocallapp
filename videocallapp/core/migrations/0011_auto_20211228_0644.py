# Generated by Django 2.2.7 on 2021-12-28 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20211228_0642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='redirect_link',
            field=models.URLField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='video_link',
            field=models.CharField(blank=True, default='', max_length=1000),
        ),
    ]