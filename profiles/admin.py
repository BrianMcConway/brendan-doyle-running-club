from django.contrib import admin
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False

class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)

    def delete_model(self, request, obj):
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
