# Generated by Django 3.0.2 on 2020-02-14 00:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0027_auto_20200213_2351'),
    ]

    operations = [
        migrations.CreateModel(
            name='Property_Applications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RenameModel(
            old_name='Properties1',
            new_name='Properties',
        ),
        migrations.DeleteModel(
            name='Property_Applications1',
        ),
        migrations.AddField(
            model_name='property_applications',
            name='listingId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Properties'),
        ),
        migrations.AddField(
            model_name='property_applications',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
