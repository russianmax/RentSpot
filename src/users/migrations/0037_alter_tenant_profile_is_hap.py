# Generated by Django 3.2.6 on 2021-08-27 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0036_alter_tenant_profile_is_hap'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tenant_profile',
            name='is_hap',
            field=models.BooleanField(null=True),
        ),
    ]