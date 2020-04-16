# Generated by Django 3.0.3 on 2020-04-13 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0024_auto_20200304_1747'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='landlord_profile',
            name='image',
        ),
        migrations.RemoveField(
            model_name='tenant_profile',
            name='image',
        ),
        migrations.RemoveField(
            model_name='tenant_profile',
            name='salary_doc',
        ),
        migrations.RemoveField(
            model_name='tenant_profile',
            name='savings_doc',
        ),
        migrations.AddField(
            model_name='landlord_profile',
            name='test',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='tenant_reviews',
            name='stars',
            field=models.IntegerField(default=5),
        ),
        migrations.AlterField(
            model_name='landlord_profile',
            name='is_landlord',
            field=models.BooleanField(choices=[(True, 'Landlord'), (False, 'Tenant')], default=True),
        ),
        migrations.AlterField(
            model_name='tenant_profile',
            name='is_hap',
            field=models.NullBooleanField(default=False),
        ),
    ]