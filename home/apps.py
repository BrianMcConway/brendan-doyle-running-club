from django.apps import AppConfig


class HomeConfig(AppConfig):
    """
    HomeConfig class that sets the configuration for the 'home' app.
    Inherits from the AppConfig base class.
    """

    default_auto_field = 'django.db.models.BigAutoField'
    
    name = 'home'