# Generated by Django 2.0.4 on 2020-03-04 17:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0030_auto_20200214_1237'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property_applications',
            name='user',
        ),
        migrations.AddField(
            model_name='property_applications',
            name='app_description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='property_applications',
            name='tenant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]