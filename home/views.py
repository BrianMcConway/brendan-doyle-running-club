from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def home(request):
    return render(request, 'home/index.html')

def about(request):
    return render(request, 'home/about.html')

def classes(request):
    return render(request, 'home/classes.html')

def contact(request):
    return render(request, 'home/contact.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            send_mail(
                f'Message from {name}',
                message,
                email,
                [settings.DEFAULT_FROM_EMAIL],
                fail_silently=False,
            )
            return redirect('contact')  # Redirect to a 'thank you' page if needed
    else:
        form = ContactForm()
    return render(request, 'home/contact.html', {'form': form})