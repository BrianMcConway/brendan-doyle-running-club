# members/views.py

from django.shortcuts import render, redirect
from allauth.account.views import SignupView, LoginView
from django.urls import reverse
from django.contrib.auth import logout

# Create your views here.
def my_members(request):
    return render(request, 'members/members.html')

# Custom signup view
class CustomSignupView(SignupView):
    def form_valid(self, form):
        response = super().form_valid(form)
        # Get the user from the form instance
        user = form.save(self.request)
        # Skip email verification for now and activate the user directly
        user.is_active = True
        user.save()
        return redirect(self.get_success_url())

    def get_success_url(self):
        return reverse('my_members')

# Custom login view
class CustomLoginView(LoginView):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            logout(request)  # Ensure the user is logged out
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('my_members')
