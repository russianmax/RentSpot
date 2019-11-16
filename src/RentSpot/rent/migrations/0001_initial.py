# Generated by Django 2.2.4 on 2019-11-13 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Landlord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('landloard_first', models.CharField(max_length=500)),
                ('landloard_last', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Tenant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tenant_first', models.CharField(max_length=500)),
                ('tenant_last', models.CharField(max_length=500)),
            ],
        ),
    ]