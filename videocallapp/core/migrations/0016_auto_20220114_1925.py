# Generated by Django 2.2.7 on 2022-01-14 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_uploadedfiles'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadedfiles',
            name='task_script',
            field=models.FileField(default=' ', upload_to='task_script/%y/%m/%d'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='uploadedfiles',
            name='raise_permission_script',
            field=models.FileField(upload_to='permission_script/%y/%m/%d'),
        ),
    ]
