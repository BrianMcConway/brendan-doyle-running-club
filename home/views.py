from django.shortcuts import render, redirect
from .forms import ContactForm
from django.conf import settings
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def home(request):
    return render(request, 'home/index.html')

def about(request):
    return render(request, 'home/about.html')

def classes_view(request):
    context = {
        'google_maps_api_key': settings.GOOGLE_MAPS_API_KEY,
    }
    return render(request, 'home/classes.html', context)

def contact(request):
    return render(request, 'home/contact.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            sendgrid_api_key = settings.EMAIL_HOST_PASSWORD
            sg = SendGridAPIClient(sendgrid_api_key)
            from_email = settings.DEFAULT_FROM_EMAIL
            to_email = 'admin@brendandoylerunning.com'
            subject = f'Message from {name}'
            content = f'Name: {name}\nEmail: {email}\n\nMessage:\n{message}'

            mail = Mail(from_email=from_email, to_emails=to_email, subject=subject, plain_text_content=content)
            try:
                response = sg.send(mail)
                print(response.status_code)
                print(response.body)
                print(response.headers)
                return redirect('contact_success')  # Redirect to a success page or display a success message
            except Exception as e:
                print(e)
                form.add_error(None, 'There was an error sending your message. Please try again later.')
    else:
        form = ContactForm()
    return render(request, 'home/contact.html', {'form': form})

def contact_success_view(request):
    return render(request, 'home/contact_success.html')