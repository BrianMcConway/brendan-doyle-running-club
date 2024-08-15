from django.urls import path
from . import views

urlpatterns = [
    path('', views.events_view, name='events_list'),
    path('<int:event_id>/', views.event_detail, name='event_detail'),
    path('<int:event_id>/book/', views.book_race, name='book_race'),
    path('booking/confirmation/<int:booking_id>/', views.booking_confirmation, name='booking_confirmation'),
    path('booking/edit/<int:booking_id>/', views.edit_booking, name='edit_booking'),
    path('booking/edit/confirmation/', views.edit_booking_confirmation, name='edit_booking_confirmation'),
    path('booking/delete/<int:booking_id>/', views.delete_booking, name='delete_booking'),
    path('booking/delete/confirmation/', views.delete_booking_confirmation, name='delete_booking_confirmation'),
    path('enter-booking-number/', views.enter_booking_number, name='enter_booking_number'),
    path('manage-booking/<str:booking_number>/', views.manage_booking, name='manage_booking'),
]
