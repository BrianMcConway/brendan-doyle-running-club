from django.urls import path
from .views import (
    home, about, classes_view, contact_view,
    contact_success_view, events_view
)

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('classes/', classes_view, name='classes'),
    path('contact/', contact_view, name='contact'),
    path(
        'contact/success/', contact_success_view,
        name='contact_success'
    ),
    path('events/', events_view, name='events_list'),
]

"""
Defines URL patterns for the home application,
mapping URLs to their respective view functions.
"""
