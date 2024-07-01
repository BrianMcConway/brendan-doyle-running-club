"""
URL configuration for running_club project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# running_club/urls.py
from django.contrib import admin
from django.urls import path, include
from home import views as home_views
from members.views import CustomSignupView, CustomLoginView, my_members

urlpatterns = [
    path('', include('home.urls')),
    path('members/', my_members, name='my_members'),
    path('admin/', admin.site.urls),
    path('account/signup/', CustomSignupView.as_view(), name='account_signup'),
    path('account/login/', CustomLoginView.as_view(), name='account_login'),
    path('account/', include('allauth.urls')),
]