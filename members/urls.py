from django.urls import path
from .views import MyMembersView, GPXFileCreateView, GPXFileEditView, GPXFileDeleteView

urlpatterns = [
    path('', MyMembersView.as_view(), name='my_members'),
    path('gpxfile/add/', GPXFileCreateView.as_view(), name='gpxfile_add'),
    path('gpxfile/<int:pk>/edit/', GPXFileEditView.as_view(), name='gpxfile_edit'),
    path('gpxfile/<int:pk>/delete/', GPXFileDeleteView.as_view(), name='gpxfile_delete'),
]
