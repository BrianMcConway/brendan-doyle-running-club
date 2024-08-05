from django.db import models

# Create your models here.

class GPXFile(models.Model):
    title = models.CharField(max_length=255)
    file_data = models.BinaryField()  # Store file data as binary

    def __str__(self):
        return self.title