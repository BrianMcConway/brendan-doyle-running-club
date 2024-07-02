from django.shortcuts import render, redirect
from allauth.account.views import SignupView, LoginView
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.db import IntegrityError

class MyMembersView(LoginRequiredMixin, TemplateView):
    template_name = 'members/members.html'
    login_url = '/account/login/'

class CustomSignupView(SignupView):
    def form_valid(self, form):
        try:
            response = super().form_valid(form)
            user = form.save(self.request)
            print(f"DEBUG: Created user: {user.username}")
            user.is_active = True
            user.save()
            return redirect(self.get_success_url())
        except IntegrityError as e:
            print(f"DEBUG: IntegrityError: {e}")
            form.add_error(None, "A user with that username already exists.")
            return self.form_invalid(form)
        except Exception as e:
            print(f"DEBUG: Other Exception: {e}")
            form.add_error(None, "An unexpected error occurred.")
            return self.form_invalid(form)

    def get_success_url(self):
        return reverse('my_members')

class CustomLoginView(LoginView):
    def get_success_url(self):
        return reverse('my_members')

def custom_logout_view(request):
    from django.contrib.auth import logout
    logout(request)
    return redirect('home')
