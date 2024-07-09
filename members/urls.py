from django.urls import path
from .views import MyMembersView

urlpatterns = [
    path('', MyMembersView.as_view(), name='my_members'),
]
