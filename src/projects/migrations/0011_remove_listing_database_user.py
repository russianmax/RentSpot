# Generated by Django 3.0.2 on 2020-02-05 20:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0010_auto_20200205_2008'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing_database',
            name='user',
        ),
    ]
