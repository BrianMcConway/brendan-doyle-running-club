from django.apps import AppConfig

class MembersConfig(AppConfig):
    """
    Configuration class for the 'members' app.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'members'

    def ready(self):
        """
        Import signals when the application is ready.
        """
        import members.signals
