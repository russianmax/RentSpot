# Generated by Django 2.2 on 2020-04-21 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0026_auto_20200420_1037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tenant_profile',
            name='hapDocument',
            field=models.FileField(blank=True, null=True, upload_to='docs'),
        ),
        migrations.AlterField(
            model_name='tenant_profile',
            name='identification',
            field=models.FileField(blank=True, null=True, upload_to='docs'),
        ),
        migrations.AlterField(
            model_name='tenant_profile',
            name='references',
            field=models.FileField(blank=True, null=True, upload_to='docs'),
        ),
        migrations.AlterField(
            model_name='tenant_profile',
            name='salaryDocument',
            field=models.FileField(blank=True, null=True, upload_to='docs'),
        ),
    ]
