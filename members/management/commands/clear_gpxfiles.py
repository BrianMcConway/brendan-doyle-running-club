from django.core.management.base import BaseCommand
from members.models import GPXFile

class Command(BaseCommand):
    help = 'Clear all GPX file entries from the database'

    def handle(self, *args, **kwargs):
        GPXFile.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Successfully cleared all GPX file entries'))
