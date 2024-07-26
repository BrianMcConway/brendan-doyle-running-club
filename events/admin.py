from django.contrib import admin
from .models import RaceEvent, Participant, Result, Booking

# Register your models here.

admin.site.register(RaceEvent)
admin.site.register(Participant)
admin.site.register(Result)
admin.site.register(Booking)