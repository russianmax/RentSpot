# Generated by Django 3.0.2 on 2020-02-02 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewListing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('propertySummary', models.CharField(max_length=100)),
                ('propertyDescription', models.TextField()),
            ],
        ),
    ]
