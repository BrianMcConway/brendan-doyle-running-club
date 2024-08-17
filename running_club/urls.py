"""
URL configuration for running_club project.
"""

from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views

from members.views import (
    CustomSignupView, CustomLoginView, MyMembersView,
    custom_logout_view, CustomPasswordResetConfirmView, CustomConfirmEmailView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('members/', include('members.urls')),
    path('profiles/', include('profiles.urls')),
    path('accounts/', include('allauth.urls')),
    path(
        'account/signup/',
        CustomSignupView.as_view(),
        name='account_signup'
    ),
    path(
        'account/login/',
        CustomLoginView.as_view(),
        name='account_login'
    ),
    path(
        'account/logout/',
        custom_logout_view,
        name='account_logout'
    ),
    path(
        'account/confirm-email/<str:key>/',
        CustomConfirmEmailView.as_view(),
        name='account_confirm_email'
    ),
    path(
        'email-verification-failed/',
        TemplateView.as_view(
            template_name='account/email_verification_failed.html'
        ),
        name='account_email_verification_failed'
    ),
    path(
        'account/email-verification-sent/',
        TemplateView.as_view(
            template_name='account/email_confirmation_sent.html'
        ),
        name='account_email_verification_sent'
    ),
    path(
        'account/email-confirmation-success/',
        TemplateView.as_view(
            template_name='account/email_confirmation_success.html'
        ),
        name='account_email_confirmation_success'
    ),
    path(
        'account/not-verified/',
        TemplateView.as_view(
            template_name='account/account_not_verified.html'
        ),
        name='account_not_verified'
    ),
    path(
        'account/email_verified_waiting_for_approval/',
        TemplateView.as_view(
            template_name='account/email_verified_waiting_for_approval.html'
        ),
        name='account_email_verified_waiting_for_approval'
    ),
    path('', include('home.urls')),
    path(
        'password_reset/',
        auth_views.PasswordResetView.as_view(
            template_name='account/password_reset.html'
        ),
        name='password_reset'
    ),
    path(
        'password_reset/done/',
        auth_views.PasswordResetDoneView.as_view(
            template_name='account/password_reset_done.html'
        ),
        name='password_reset_done'
    ),
    path(
        'reset/<uidb64>/<token>/',
        CustomPasswordResetConfirmView.as_view(),
        name='password_reset_confirm'
    ),
    path(
        'reset/done/',
        auth_views.PasswordResetCompleteView.as_view(
            template_name='account/password_reset_complete.html'
        ),
        name='password_reset_complete'
    ),
]

"""
Defines URL patterns for the running_club project,mapping
URLs to their respective view functions and templates.
"""
