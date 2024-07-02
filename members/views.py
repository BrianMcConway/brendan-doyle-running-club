from django.shortcuts import render, redirect
from allauth.account.views import SignupView, LoginView
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

class MyMembersView(LoginRequiredMixin, TemplateView):
    template_name = 'members/members.html'
    login_url = '/account/login/'

class CustomSignupView(SignupView):
    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save(self.request)
        user.is_active = True
        user.save()
        return redirect(self.get_success_url())

    def get_success_url(self):
        return reverse('my_members')

class CustomLoginView(LoginView):
    def get_success_url(self):
        return reverse('my_members')

def custom_logout_view(request):
    from django.contrib.auth import logout
    logout(request)
    return redirect('home')
