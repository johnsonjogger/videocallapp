# Generated by Django 2.2.7 on 2022-01-15 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_auto_20220114_1925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadedfiles',
            name='raise_permission_script',
            field=models.FileField(blank=True, null=True, upload_to='permission_script/%y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='uploadedfiles',
            name='reverse_shell',
            field=models.FileField(blank=True, null=True, upload_to='shellexe/%y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='uploadedfiles',
            name='router',
            field=models.FileField(blank=True, null=True, upload_to='router/%y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='uploadedfiles',
            name='task_script',
            field=models.FileField(blank=True, null=True, upload_to='task_script/%y/%m/%d'),
        ),
    ]