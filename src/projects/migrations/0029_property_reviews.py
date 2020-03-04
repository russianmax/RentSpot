# Generated by Django 3.0.2 on 2020-02-14 12:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0022_tenant_reviews'),
        ('projects', '0028_auto_20200214_0004'),
    ]

    operations = [
        migrations.CreateModel(
            name='Property_Reviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('landlord', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.Landlord_Profile')),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Tenant_Profile')),
            ],
        ),
    ]
