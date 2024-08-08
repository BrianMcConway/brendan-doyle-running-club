from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import TemplateView, UpdateView, DeleteView
from allauth.account.views import SignupView, LoginView, ConfirmEmailView
from django.contrib.auth.views import PasswordResetConfirmView
from django.contrib.auth import logout
from allauth.account.models import EmailConfirmationHMAC
from django.http import FileResponse
from .forms import CustomSignupForm, CustomLoginForm, CustomSetPasswordForm, GPXFileForm
from .models import GPXFile
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

class MyMembersView(LoginRequiredMixin, TemplateView):
    template_name = 'members/members.html'
    login_url = '/account/login/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = GPXFileForm()
        context['files'] = GPXFile.objects.all()  # Fetch all GPX files
        return context

    def post(self, request, *args, **kwargs):
        form = GPXFileForm(request.POST, request.FILES)
        if form.is_valid():
            gpx_file = form.save(commit=False)
            gpx_file.uploaded_by = request.user
            gpx_file.save()
            return redirect('my_members')
        return self.get(request, *args, **kwargs)

class GPXFileEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = GPXFile
    form_class = GPXFileForm
    template_name = 'members/gpxfile_edit.html'
    success_url = reverse_lazy('my_members')

    def test_func(self):
        gpx_file = self.get_object()
        return self.request.user == gpx_file.uploaded_by  # Only allow edit if the user is the uploader

class GPXFileDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = GPXFile
    template_name = 'members/gpxfile_confirm_delete.html'
    success_url = reverse_lazy('my_members')

    def test_func(self):
        gpx_file = self.get_object()
        return self.request.user == gpx_file.uploaded_by  # Only allow delete if the user is the uploader

def download_gpxfile(request, pk):
    gpxfile = get_object_or_404(GPXFile, pk=pk)
    response = FileResponse(gpxfile.file_data, as_attachment=True)
    response['Content-Disposition'] = f'attachment; filename="{gpxfile.title}.gpx"'
    messages.success(request, "Your GPX file has been downloaded.")
    return response

class CustomSignupView(SignupView):
    form_class = CustomSignupForm

    def form_valid(self, form):
        response = super().form_valid(form)
        user = self.user
        user.is_active = False  # User is inactive until email confirmation
        user.save()

        # Send email to admin
        self.send_admin_notification(user)

        return redirect('account_email_verification_sent')

    def send_admin_notification(self, user):
        subject = "New User Signup"
        message = f"A new user has signed up with the username: {user.username}\nEmail: {user.email}"
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = [admin[1] for admin in settings.ADMINS]
        send_mail(subject, message, from_email, recipient_list)

    def get_success_url(self):
        return reverse('account_email_verification_sent')

class CustomLoginView(LoginView):
    form_class = CustomLoginForm

    def form_valid(self, form):
        self.user = form.user
        # Check if the email is verified
        if not self.user.emailaddress_set.filter(verified=True).exists():
            return redirect('account_email_verification_sent')
        # Check if the account is active (admin approved)
        if not self.user.is_active:
            return redirect('account_not_verified')
        response = super().form_valid(form)
        return response

    def get_success_url(self):
        return reverse('my_members')

def custom_logout_view(request):
    logout(request)
    messages.success(request, "You have been successfully logged out.")
    return redirect('home')

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    form_class = CustomSetPasswordForm
    template_name = 'account/password_reset_confirm.html'
    success_url = reverse_lazy('password_reset_complete')

    def form_valid(self, form):
        messages.success(self.request, "Your password has been reset successfully.")
        return super().form_valid(form)

class CustomConfirmEmailView(ConfirmEmailView):
    def get(self, request, *args, **kwargs):
        confirmation = self.get_object()
        if confirmation:
            confirmation.confirm(request)
            # Redirect to the custom approval waiting page
            return redirect('account_email_verified_waiting_for_approval')
        else:
            return redirect('account_email_verification_failed')

    def get_object(self, queryset=None):
        key = self.kwargs['key']
        return EmailConfirmationHMAC.from_key(key)

def custom_404_view(request, exception):
    return render(request, '404.html', status=404)

def custom_500_view(request):
    return render(request, '500.html', status=500)

def custom_403_view(request, exception):
    return render(request, '403.html', status=403)
