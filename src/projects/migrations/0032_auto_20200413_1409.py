# Generated by Django 3.0.3 on 2020-04-13 13:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0025_auto_20200413_1409'),
        ('projects', '0031_auto_20200304_1747'),
    ]

    operations = [
        migrations.RenameField(
            model_name='property_applications',
            old_name='listingId',
            new_name='listing',
        ),
        migrations.RemoveField(
            model_name='property_applications',
            name='tenant',
        ),
        migrations.RemoveField(
            model_name='property_reviews',
            name='created_on',
        ),
        migrations.AddField(
            model_name='property_applications',
            name='created',
            field=models.TextField(default=1),
        ),
        migrations.AddField(
            model_name='property_applications',
            name='property_owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.Landlord_Profile'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='property_applications',
            name='tenant_apply',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.Tenant_Profile'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='property_reviews',
            name='created',
            field=models.TextField(default=1),
        ),
        migrations.AddField(
            model_name='property_reviews',
            name='landlord',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.Landlord_Profile'),
        ),
        migrations.AlterField(
            model_name='property_applications',
            name='app_description',
            field=models.TextField(default='app description'),
        ),
        migrations.AlterField(
            model_name='property_reviews',
            name='tenant',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.Tenant_Profile'),
        ),
    ]
