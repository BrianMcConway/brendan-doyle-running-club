from django.contrib import admin
from .models import GPXFile
from django.contrib.auth.models import User


@admin.action(description='Approve selected users')
def approve_users(modeladmin, request, queryset):
    """
    Custom admin action to approve selected users by setting
    their is_active status to True.
    """
    queryset.update(is_active=True)


class UserAdmin(admin.ModelAdmin):
    """
    Custom admin model for User with specified list display and actions.
    """
    list_display = ('username', 'email', 'is_active', 'is_staff')
    actions = [approve_users]


admin.site.unregister(User)
admin.site.register(User, UserAdmin)


class GPXFileAdmin(admin.ModelAdmin):
    """
    Custom admin model for GPXFile with specified
    list display and custom method.
    """
    list_display = ('id', 'title', 'has_file')

    def has_file(self, obj):
        """
        Custom method to check if a GPXFile object has associated file data.
        """
        return bool(obj.file_data)

    has_file.boolean = True
    has_file.short_description = 'Has File'


admin.site.register(GPXFile, GPXFileAdmin)
