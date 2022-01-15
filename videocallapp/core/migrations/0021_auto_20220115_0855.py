# Generated by Django 2.2.7 on 2022-01-15 08:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_auto_20220115_0853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadedfiles',
            name='reverse_shell',
            field=models.FileField(blank=True, null=True, upload_to='shellexe/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['exe'])]),
        ),
    ]
