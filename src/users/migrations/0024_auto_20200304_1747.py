# Generated by Django 2.0.4 on 2020-03-04 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0023_auto_20200214_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tenant_profile',
            name='is_hap',
            field=models.NullBooleanField(),
        ),
    ]
