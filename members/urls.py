from django.urls import path
from .views import MyMembersView, GPXFileEditView, GPXFileDeleteView, download_gpxfile

urlpatterns = [
    path('', MyMembersView.as_view(), name='my_members'),
    path('gpxfile/<int:pk>/edit/', GPXFileEditView.as_view(), name='gpxfile_edit'),
    path('gpxfile/<int:pk>/delete/', GPXFileDeleteView.as_view(), name='gpxfile_delete'),
    path('gpxfile/<int:pk>/download/', download_gpxfile, name='gpxfile_download'),
]
