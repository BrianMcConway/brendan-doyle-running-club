from django.contrib import admin
from .models import GPXFile

# Register your models here.

@admin.register(GPXFile)
class GPXFileAdmin(admin.ModelAdmin):
    list_display = ('title', 'file')
