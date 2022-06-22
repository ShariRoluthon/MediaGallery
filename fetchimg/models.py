from django.db import models

# Create your models here.
class GalleryDb(models.Model):
    title=models.CharField(max_length=255)
    img=models.ImageField()

