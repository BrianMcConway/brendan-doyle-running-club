from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    ProfileDetailView, ProfileCreateView,
    ProfileUpdateView, ProfileDeleteView
)
from .forms import CustomPasswordChangeForm

urlpatterns = [
    path('', ProfileDetailView.as_view(), name='profile_detail'),
    path('new/', ProfileCreateView.as_view(), name='profile_create'),
    path('edit/', ProfileUpdateView.as_view(), name='profile_update'),
    path('delete/', ProfileDeleteView.as_view(), name='profile_delete'),
    path(
        'password_change/',
        auth_views.PasswordChangeView.as_view(
            template_name='profiles/password_change_form.html',
            form_class=CustomPasswordChangeForm
        ),
        name='password_change'
    ),
    path(
        'password_change/done/',
        auth_views.PasswordChangeDoneView.as_view(
            template_name='profiles/password_change_done.html'
        ),
        name='password_change_done'
    ),
]

"""
Defines URL patterns for the profiles application,
mapping URLs to their respective view functions and templates.
"""
