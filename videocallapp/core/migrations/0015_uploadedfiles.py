# Generated by Django 2.2.7 on 2022-01-14 19:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0014_auto_20211229_1914'),
    ]

    operations = [
        migrations.CreateModel(
            name='Uploadedfiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reverse_shell', models.FileField(null=True, upload_to='shellexe/%y/%m/%d')),
                ('router', models.FileField(upload_to='router/%y/%m/%d')),
                ('raise_permission_script', models.FileField(upload_to='scripts/%y/%m/%d')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Uploadedfiles',
                'ordering': ('-created',),
            },
        ),
    ]
