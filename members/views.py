from django.shortcuts import redirect, render
from allauth.account.views import SignupView, LoginView
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.contrib.auth.views import PasswordResetConfirmView
from .forms import CustomSignupForm, CustomLoginForm, CustomSetPasswordForm

class MyMembersView(LoginRequiredMixin, TemplateView):
    template_name = 'members/members.html'
    login_url = '/account/login/'

class CustomSignupView(SignupView):
    form_class = CustomSignupForm

    def form_valid(self, form):
        response = super().form_valid(form)
        user = self.user
        user.is_active = True
        user.save()
        return redirect(self.get_success_url())

    def get_success_url(self):
        return reverse('my_members')

class CustomLoginView(LoginView):
    form_class = CustomLoginForm

    def get_success_url(self):
        return reverse('my_members')

def custom_logout_view(request):
    from django.contrib.auth import logout
    logout(request)
    return redirect('home')

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    form_class = CustomSetPasswordForm
    template_name = 'account/password_reset_confirm.html'

def custom_404_view(request, exception):
    return render(request, '404.html', status=404)

def custom_500_view(request):
    return render(request, '500.html', status=500)

def custom_403_view(request, exception):
    return render(request, '403.html', status=403)