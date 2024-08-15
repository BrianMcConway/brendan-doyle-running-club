from django.db import migrations, models
from django.contrib.auth.models import User

def fill_null_users(apps, schema_editor):
    Booking = apps.get_model('events', 'Booking')
    
    default_user = User.objects.first()
    if not default_user:
        raise Exception('No default user found. Please create a user first.')

    null_user_bookings = Booking.objects.filter(user__isnull=True)
    null_user_bookings.update(user=default_user)

class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_alter_booking_user'),
    ]

    operations = [
        migrations.RunPython(fill_null_users),
        migrations.AlterField(
            model_name='booking',
            name='user',
            field=models.ForeignKey(on_delete=models.CASCADE, to='auth.User', default=1),
            preserve_default=False,
        ),
    ]
