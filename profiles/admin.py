from django.contrib import admin
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

class ProfileInline(admin.StackedInline):
    """
    Defines an inline admin descriptor for Profile model.
    """
    model = Profile
    can_delete = False

class UserAdmin(BaseUserAdmin):
    """
    Extends the default UserAdmin to include Profile inline.
    """
    inlines = (ProfileInline,)

    def delete_model(self, request, obj):
        """
        Deletes the associated Profile when a User is deleted.
        """
        if isinstance(obj, User):
            try:
                profile = Profile.objects.get(user=obj)
                profile.delete()
            except Profile.DoesNotExist:
                pass
        super().delete_model(request, obj)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Profile)
