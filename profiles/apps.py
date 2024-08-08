from django.apps import AppConfig

class ProfilesConfig(AppConfig):
    """
    Configuration for the Profiles app.
    """
    name = 'profiles'

    def ready(self):
        """
        Import signals to ensure they are registered when the app is ready.
        """
        import profiles.signals
