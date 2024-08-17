from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from .models import Profile
from .forms import ProfileForm, UserForm
from django.contrib.auth import logout
from django.contrib import messages


class ProfileDetailView(LoginRequiredMixin, DetailView):
    """
    View for displaying the profile details of the logged-in user.
    """
    model = Profile
    template_name = 'profiles/profile_detail.html'

    def get_object(self):
        """
        Returns the profile object for the logged-in user.
        Raises PermissionDenied if the user account is not active.
        """
        profile = get_object_or_404(Profile, user=self.request.user)
        if not self.request.user.is_active:
            raise PermissionDenied(
                "Your account is not active."
            )
        return profile


class ProfileCreateView(LoginRequiredMixin, CreateView):
    """
    View for creating a new profile for the logged-in user.
    """
    model = Profile
    form_class = ProfileForm
    template_name = 'profiles/profile_form.html'
    success_url = reverse_lazy('profile_detail')

    def get_context_data(self, **kwargs):
        """
        Adds the user form to the context data.
        """
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['user_form'] = UserForm(
                self.request.POST, instance=self.request.user
            )
        else:
            context['user_form'] = UserForm(instance=self.request.user)
        return context

    def form_valid(self, form):
        """
        Validates the profile form and the user form.
        If both forms are valid, saves the profile and user data.
        """
        if not self.request.user.is_active:
            raise PermissionDenied(
                "Your account is not active."
            )

        context = self.get_context_data()
        user_form = context['user_form']
        if user_form.is_valid():
            self.object = form.save(commit=False)
            self.object.user = self.request.user
            user_form.save()
            self.object.save()
            messages.success(
                self.request, 'Profile successfully created!'
            )
            return redirect(self.get_success_url())
        else:
            messages.error(
                self.request, 'There was an error creating your profile.'
            )
            return self.form_invalid(form)


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    """
    View for updating the profile of the logged-in user.
    """
    model = Profile
    form_class = ProfileForm
    template_name = 'profiles/profile_form.html'
    success_url = reverse_lazy('profile_detail')

    def get_object(self):
        """
        Returns the profile object for the logged-in user.
        Raises PermissionDenied if the user account is not active.
        """
        profile = get_object_or_404(Profile, user=self.request.user)
        if not self.request.user.is_active:
            raise PermissionDenied(
                "Your account is not active."
            )
        return profile

    def get_context_data(self, **kwargs):
        """
        Adds the user form to the context data.
        """
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['user_form'] = UserForm(
                self.request.POST, instance=self.request.user
            )
        else:
            context['user_form'] = UserForm(instance=self.request.user)
        return context

    def form_valid(self, form):
        """
        Validates the profile form and the user form.
        If both forms are valid, saves the profile and user data.
        """
        if not self.request.user.is_active:
            raise PermissionDenied(
                "Your account is not active."
            )

        context = self.get_context_data()
        user_form = context['user_form']
        if user_form.is_valid():
            user_form.save()
            form.save()
            messages.success(
                self.request, 'Profile successfully updated!'
            )
            return redirect(self.get_success_url())
        else:
            messages.error(
                self.request, 'There was an error updating your profile.'
            )
            return self.form_invalid(form)


class ProfileDeleteView(LoginRequiredMixin, DeleteView):
    """
    View for deleting the profile of the logged-in user.
    """
    model = Profile
    template_name = 'profiles/profile_confirm_delete.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        """
        Returns the profile object for the logged-in user.
        Raises PermissionDenied if the user account is not active.
        """
        profile = get_object_or_404(Profile, user=self.request.user)
        if not self.request.user.is_active:
            raise PermissionDenied(
                "Your account is not active."
            )
        return profile

    def delete(self, request, *args, **kwargs):
        """
        Deletes the profile and logs out the user.
        """
        profile = self.get_object()
        profile.delete()
        messages.success(self.request, 'Profile successfully deleted.')
        logout(request)
        return redirect(self.success_url)