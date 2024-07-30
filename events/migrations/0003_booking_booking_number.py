# Generated by Django 5.0.6 on 2024-07-30 11:41

from django.db import migrations, models
import uuid

class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_alter_raceevent_distance_booking'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='booking_number',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]