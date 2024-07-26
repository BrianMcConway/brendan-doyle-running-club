from django.urls import path
from . import views

urlpatterns = [
    path('', views.events_view, name='events_list'),
    path('<int:event_id>/', views.event_detail, name='event_detail'),
    path('<int:event_id>/book/', views.book_race, name='book_race'),
    path('booking/confirmation/<int:booking_id>/', views.booking_confirmation, name='booking_confirmation'),
]
