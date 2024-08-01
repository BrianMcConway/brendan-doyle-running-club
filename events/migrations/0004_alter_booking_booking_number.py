# Generated by Django 5.0.6 on 2024-07-30 11:43

from django.db import migrations, models
import uuid

def generate_unique_booking_numbers(apps, schema_editor):
    Booking = apps.get_model('events', 'Booking')
    for booking in Booking.objects.all():
        booking.booking_number = uuid.uuid4()
        booking.save()

class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_booking_booking_number'),
    ]

    operations = [
        migrations.RunPython(generate_unique_booking_numbers),
        migrations.AlterField(
            model_name='booking',
            name='booking_number',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]