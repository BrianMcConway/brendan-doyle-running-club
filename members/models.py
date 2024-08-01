from django.db import models
from cloudinary_storage.storage import RawMediaCloudinaryStorage

# Create your models here.

class GPXFile(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(storage=RawMediaCloudinaryStorage(), upload_to='gpx_files/')

    def __str__(self):
        return self.title
