# Generated by Django 2.2.7 on 2021-12-28 14:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20211228_0634'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CokeBottleUserProfile',
            new_name='UserProfile',
        ),
        migrations.DeleteModel(
            name='NadiaUserProfile',
        ),
        migrations.AlterModelOptions(
            name='userprofile',
            options={'ordering': ('-created',), 'verbose_name_plural': 'UserProfiles'},
        ),
    ]