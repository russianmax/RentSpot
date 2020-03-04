# Generated by Django 3.0.2 on 2020-02-13 23:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0021_auto_20200212_1920'),
    ]

    operations = [
        migrations.CreateModel(
            name='Properties',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=100)),
                ('rentPrice', models.IntegerField()),
                ('description', models.TextField()),
                ('bedRooms', models.IntegerField()),
                ('bathRoom', models.IntegerField()),
                ('tenantCondtions', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='house_preview/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RenameModel(
            old_name='Listing_Applications',
            new_name='Property_Applications',
        ),
        migrations.DeleteModel(
            name='Listing_Database',
        ),
        migrations.AlterField(
            model_name='property_applications',
            name='listingId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Properties'),
        ),
    ]
