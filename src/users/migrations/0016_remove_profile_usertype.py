# Generated by Django 3.0.2 on 2020-02-08 18:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_profile_usertype'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='usertype',
        ),
    ]
