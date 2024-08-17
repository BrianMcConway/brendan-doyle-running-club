from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from profiles.models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """
    Create a user profile and send an email notification
    when a new user is created.
    """
    if created:
        Profile.objects.get_or_create(user=instance)
        send_mail(
            subject='New User Signed Up',
            message=f'User {instance.username} has signed up.',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[admin[1] for admin in settings.ADMINS]
        )


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    """
    Save the user profile after the user object is saved.
    """
    instance.profile.save()
