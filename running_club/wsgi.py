"""
WSGI config for running_club project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

# Set the default settings module for the 'running_club' project
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'running_club.settings')

# Get the WSGI application for the 'running_club' project
application = get_wsgi_application()
