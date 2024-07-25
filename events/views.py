from django.shortcuts import render, get_object_or_404
from .models import RaceEvent

# Create your views here.

def events_view(request):
    events = RaceEvent.objects.all().order_by('date')
    return render(request, 'events/events.html', {'events': events})

def event_detail(request, event_id):
    event = get_object_or_404(RaceEvent, pk=event_id)
    return render(request, 'events/event_detail.html', {'event': event})
