# Generated by Django 2.2.7 on 2021-12-16 09:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20211216_0143'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cokebottleuserprofile',
            options={'ordering': ('-created',), 'verbose_name_plural': 'Short_Coke_Bottle__Profiles'},
        ),
        migrations.AlterModelOptions(
            name='curzeuserprofile',
            options={'ordering': ('created',), 'verbose_name_plural': 'Curze__Profiles'},
        ),
        migrations.AlterModelOptions(
            name='nadiauserprofile',
            options={'ordering': ('created',), 'verbose_name_plural': 'Nadia_Profile'},
        ),
    ]
