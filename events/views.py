from django.shortcuts import render, redirect, get_object_or_404
from .models import RaceEvent, Booking
from .forms import BookingForm

# Create your views here.

def events_view(request):
    events = RaceEvent.objects.all().order_by('date')
    return render(request, 'events/events.html', {'events': events})

def event_detail(request, event_id):
    event = get_object_or_404(RaceEvent, pk=event_id)
    return render(request, 'events/event_detail.html', {'event': event})

def book_race(request, event_id):
    race = get_object_or_404(RaceEvent, pk=event_id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('booking_confirmation', booking_id=form.instance.id)
    else:
        form = BookingForm(initial={'race': race})
    return render(request, 'events/book_race.html', {'form': form, 'race': race})

def booking_confirmation(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id)
    return render(request, 'events/booking_confirmation.html', {'booking': booking})
