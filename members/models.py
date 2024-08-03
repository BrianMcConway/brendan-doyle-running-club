from django.db import models

# Create your models here.

class GPXFile(models.Model):
    title = models.CharField(max_length=100)
    file = models.BinaryField()

    def __str__(self):
        return self.title