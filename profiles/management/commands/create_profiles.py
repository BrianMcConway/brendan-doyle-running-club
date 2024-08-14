from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from profiles.models import Profile

class Command(BaseCommand):
    """
    Management command to create profiles for users who do not have profiles.
    """
    help = 'Create profiles for users without profiles'

    def handle(self, *args, **kwargs):
        """
        Handle the command execution.
        """
        users = User.objects.filter(profile__isnull=True)
        for user in users:
            Profile.objects.create(user=user)
            self.stdout.write(self.style.SUCCESS(f'Created profile for {user.username}'))
