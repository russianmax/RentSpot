# Generated by Django 3.0.3 on 2020-02-06 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20200205_2052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='usertype',
            field=models.BooleanField(choices=[(1, 'Landlord'), (2, 'Tenant')], default=1),
        ),
    ]
