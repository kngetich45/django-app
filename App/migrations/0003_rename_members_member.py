# Generated by Django 4.0.4 on 2022-07-10 12:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_rename_users_members'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Members',
            new_name='Member',
        ),
    ]