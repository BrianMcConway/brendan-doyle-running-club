# Generated by Django 5.0.6 on 2024-08-14 10:19

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_alter_gpxfile_uploaded_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='gpxfile',
            name='uploaded_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]