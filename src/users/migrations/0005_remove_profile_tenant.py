# Generated by Django 3.0.3 on 2020-02-05 19:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_profile_tenant'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='tenant',
        ),
    ]
