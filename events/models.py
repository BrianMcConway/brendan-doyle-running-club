import random
import string
from django.db import models

class RaceEvent(models.Model):
    DISTANCE_CHOICES = [
        ('10K', '10K'),
        ('HM', 'Half Marathon'),
        ('M', 'Marathon'),
        ('53K', '53K Ultra Marathon'),
    ]

    name = models.CharField(max_length=255, default='The Royal Canal Run Longford')
    year = models.IntegerField()
    date = models.DateField()
    distance = models.CharField(max_length=3, choices=DISTANCE_CHOICES)
    location = models.CharField(max_length=255, default='Longford')
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} {self.year} - {self.get_distance_display()}"

class Participant(models.Model):
    event = models.ForeignKey(RaceEvent, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.event}"

class Result(models.Model):
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    finish_time = models.DurationField()
    race_date = models.DateField()

    def __str__(self):
        return f"{self.participant} - {self.finish_time}"

class Booking(models.Model):
    race = models.ForeignKey(RaceEvent, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    booking_date = models.DateTimeField(auto_now_add=True)
    booking_number = models.CharField(max_length=20, unique=True, editable=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name} booked {self.race.name} on {self.booking_date}"

    def save(self, *args, **kwargs):
        if not self.booking_number:
            self.booking_number = self.generate_booking_number()
        super().save(*args, **kwargs)

    def generate_booking_number(self):
        prefix = "RCRL-25-"
        suffix = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        return f"{prefix}{suffix}"