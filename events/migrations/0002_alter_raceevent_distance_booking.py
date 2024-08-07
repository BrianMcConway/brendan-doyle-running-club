# Generated by Django 5.0.6 on 2024-07-25 16:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='raceevent',
            name='distance',
            field=models.CharField(choices=[('10K', '10K'), ('HM', 'Half Marathon'), ('M', 'Marathon'), ('53K', '53K Ultra Marathon')], max_length=3),
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('booking_date', models.DateTimeField(auto_now_add=True)),
                ('race', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.raceevent')),
            ],
        ),
    ]
