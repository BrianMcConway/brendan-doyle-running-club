from django.urls import path
from .views import home, about, classes_view, contact_view, contact_success_view

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('classes/', classes_view, name='classes'),
    path('contact/', contact_view, name='contact'),
    path('contact/success/', contact_success_view, name='contact_success'),
]
"""
Defines URL patterns for the application, mapping URLs to their respective view functions.
"""