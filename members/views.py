from django.http import HttpResponse, FileResponse
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
    """
    View to display the members page with GPX file upload and listing.
    """
    template_name = 'members/members.html'
    login_url = '/account/login/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = GPXFileForm()
        context['files'] = GPXFile.objects.all().order_by('-uploaded_at')
        return context

    def post(self, request, *args, **kwargs):
        form = GPXFileForm(request.POST, request.FILES)
        if form.is_valid():
            gpx_file = form.save(commit=False)
            gpx_file.uploaded_by = request.user
            gpx_file.save()
            messages.success(request, "GPX file uploaded successfully.")
            return redirect('my_members')
        else:
            messages.error(request, "There was an error uploading the GPX file.")
        return self.get(request, *args, **kwargs)

class GPXFileEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    View to edit a GPX file if the user is the uploader.
    """
    model = GPXFile
    form_class = GPXFileForm
    template_name = 'members/gpxfile_edit.html'
    success_url = reverse_lazy('my_members')

    def test_func(self):
        gpx_file = self.get_object()
        return self.request.user == gpx_file.uploaded_by

    def form_valid(self, form):
        messages.success(self.request, "GPX file updated successfully.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "There was an error updating the GPX file.")
        return super().form_invalid(form)

class GPXFileDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    View to delete a GPX file if the user is the uploader.
    """
    model = GPXFile
    template_name = 'members/gpxfile_confirm_delete.html'
    success_url = reverse_lazy('my_members')

    def test_func(self):
        gpx_file = self.get_object()
        return self.request.user == gpx_file.uploaded_by

    def delete(self, request, *args, **kwargs):
        messages.success(request, "GPX file deleted successfully.")
        return super().delete(request, *args, **kwargs)

def download_gpxfile(request, pk):
    """
    View to handle downloading a GPX file.
    """
    gpxfile = get_object_or_404(GPXFile, pk=pk)
    response = HttpResponse(gpxfile.file_data, content_type='application/gpx+xml')
    response['Content-Disposition'] = f'attachment; filename="{gpxfile.title}.gpx"'
    messages.success(request, "Your GPX file has been downloaded.")
    return response

class CustomSignupView(SignupView):
    """
    Custom signup view to handle new user registration and email notification to admin.
    """
    form_class = CustomSignupForm

    def form_valid(self, form):
        response = super().form_valid(form)
        user = self.user
        user.is_active = False
        user.save()
        self.send_admin_notification(user)
        messages.success(self.request, "Your account has been created. Please verify your email.")
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
    """
    Custom login view to handle user login and check email verification and account activation.
    """
    form_class = CustomLoginForm

    def form_valid(self, form):
        self.user = form.user
        if not self.user.emailaddress_set.filter(verified=True).exists():
            messages.warning(self.request, "Please verify your email before logging in.")
            return redirect('account_email_verification_sent')
        if not self.user.is_active:
            messages.error(self.request, "Your account is not activated. Please contact support.")
            return redirect('account_not_verified')
        messages.success(self.request, "You have logged in successfully.")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('my_members')

def custom_logout_view(request):
    """
    Custom logout view to handle user logout and display a success message.
    """
    logout(request)
    messages.success(request, "You have been successfully logged out.")
    return redirect('home')

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    """
    Custom password reset confirm view to handle password reset confirmation.
    """
    form_class = CustomSetPasswordForm
    template_name = 'account/password_reset_confirm.html'
    success_url = reverse_lazy('password_reset_complete')

    def form_valid(self, form):
        messages.success(self.request, "Your password has been reset successfully.")
        return super().form_valid(form)

class CustomConfirmEmailView(ConfirmEmailView):
    """
    Custom confirm email view to handle email confirmation and account activation.
    """
    def get(self, request, *args, **kwargs):
        confirmation = self.get_object()
        if confirmation:
            confirmation.confirm(request)
            messages.success(request, "Your email has been confirmed. Please wait for account activation.")
            return redirect('account_email_verified_waiting_for_approval')
        else:
            messages.error(request, "Email confirmation failed. Please try again.")
            return redirect('account_email_verification_failed')

    def get_object(self, queryset=None):
        key = self.kwargs['key']
        return EmailConfirmationHMAC.from_key(key)

def custom_404_view(request, exception):
    """
    Custom view to handle 404 errors.
    """
    messages.error(request, "The page you are looking for could not be found.")
    return render(request, '404.html', status=404)

def custom_500_view(request):
    """
    Custom view to handle 500 errors.
    """
    messages.error(request, "An internal server error occurred.")
    return render(request, '500.html', status=500)

def custom_403_view(request, exception):
    """
    Custom view to handle 403 errors.
    """
    messages.error(request, "You do not have permission to view this page.")
    return render(request, '403.html', status=403)
