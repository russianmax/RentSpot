# Generated by Django 3.0.2 on 2020-02-09 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_remove_profile_usertype'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='usertype',
            field=models.BooleanField(choices=[(True, 'Landlord'), (False, 'Tenant')], default=False),
        ),
    ]
