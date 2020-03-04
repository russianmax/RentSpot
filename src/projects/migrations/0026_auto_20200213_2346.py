# Generated by Django 3.0.2 on 2020-02-13 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0025_delete_property_applications'),
    ]

    operations = [
        migrations.RenameField(
            model_name='properties',
            old_name='user',
            new_name='landlord',
        ),
        migrations.AlterField(
            model_name='properties',
            name='rentPrice',
            field=models.FloatField(),
        ),
    ]