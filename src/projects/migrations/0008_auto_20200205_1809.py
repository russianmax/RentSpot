# Generated by Django 3.0.2 on 2020-02-05 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_auto_20200205_1141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing_database',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='media/house_preview/'),
        ),
    ]
