# Generated by Django 3.0.2 on 2020-02-06 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0013_listing_images_listingid'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing_database',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='house_preview'),
        ),
        migrations.DeleteModel(
            name='Listing_Images',
        ),
    ]