# Generated by Django 5.0.6 on 2024-08-15 19:20

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='booking',
            unique_together={('user', 'race')},
        ),
    ]