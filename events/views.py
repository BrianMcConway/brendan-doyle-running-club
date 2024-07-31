from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import RaceEvent, Booking
from .forms import BookingForm
from django.core.mail import send_mail
from django.conf import settings

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
            booking = form.save(commit=False)
            booking.save()
            # Send email with booking number and race distance
            send_mail(
                'Your Race Booking Confirmation',
                f'Thank you for booking {booking.race.name} ({booking.race.get_distance_display()}). Your booking number is {booking.booking_number}.',
                settings.DEFAULT_FROM_EMAIL,
                [booking.email],
                fail_silently=False,
            )
            return redirect('booking_confirmation', booking_id=booking.id)
    else:
        form = BookingForm(initial={'race': race})
    return render(request, 'events/book_race.html', {'form': form, 'race': race})

def booking_confirmation(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id)
    return render(request, 'events/booking_confirmation.html', {'booking': booking})

def enter_booking_number(request):
    error_message = None
    if request.method == 'POST':
        booking_number = request.POST.get('booking_number')
        if Booking.objects.filter(booking_number=booking_number).exists():
            return redirect('manage_booking', booking_number=booking_number)
        else:
            error_message = "No booking found. Please make sure you have entered the correct booking number."
    return render(request, 'events/enter_booking_number.html', {'error_message': error_message})


def manage_booking(request, booking_number=None):
    booking = None
    error_message = None
    if request.method == 'POST':
        booking_number = request.POST.get('booking_number')
        try:
            booking = Booking.objects.get(booking_number=booking_number)
        except Booking.DoesNotExist:
            error_message = "No booking found. Please make sure you have entered the correct booking number."
    elif booking_number:
        try:
            booking = Booking.objects.get(booking_number=booking_number)
        except Booking.DoesNotExist:
            error_message = "No booking found. Please make sure you have entered the correct booking number."
    return render(request, 'events/manage_booking.html', {'booking': booking, 'error_message': error_message})

def edit_booking(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('edit_booking_confirmation')
    else:
        form = BookingForm(instance=booking)
    return render(request, 'events/edit_booking.html', {'form': form, 'booking': booking})

def delete_booking(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id)
    if request.method == 'POST':
        booking.delete()
        return redirect('delete_booking_confirmation')
    return render(request, 'events/confirm_delete_booking.html', {'booking': booking, 'manage_booking_url': reverse('manage_booking', args=[booking.booking_number])})

def edit_booking_confirmation(request):
    return render(request, 'events/edit_booking_confirmation.html')

def delete_booking_confirmation(request):
    return render(request, 'events/delete_booking_confirmation.html')
