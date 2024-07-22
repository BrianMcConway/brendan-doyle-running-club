from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('classes/', views.classes_view, name='classes'),
    path('contact/', views.contact_view, name='contact'),
]
