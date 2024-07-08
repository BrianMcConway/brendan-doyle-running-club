from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver, Signal
from .models import Profile

class ProfileSignal:
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()