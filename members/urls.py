from django.urls import path
from .views import ProfileDetailView, ProfileCreateView, ProfileUpdateView, ProfileDeleteView

urlpatterns = [
    path('', ProfileDetailView.as_view(), name='profile_detail'),
    path('new/', ProfileCreateView.as_view(), name='profile_create'),
    path('edit/', ProfileUpdateView.as_view(), name='profile_update'),
    path('delete/', ProfileDeleteView.as_view(), name='profile_delete'),
]