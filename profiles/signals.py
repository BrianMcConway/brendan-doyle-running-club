from django.db.models.signals import post_save, post_delete
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Signal to create a Profile instance when a new User is created.
    This signal is triggered after a User instance is saved.
    """
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """
    Signal to save the Profile instance when the User is saved.
    Ensures the related Profile instance is updated whenever the 
    User instance is updated.
    """
    instance.profile.save()


@receiver(post_delete, sender=Profile)
def delete_user(sender, instance, **kwargs):
    """
    Signal to delete the User instance when the Profile is deleted.
    Ensures that when a Profile is deleted, the associated User 
    is also deleted.
    """
    instance.user.delete()
