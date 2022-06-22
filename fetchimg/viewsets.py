from rest_framework import viewsets
from . import models
from . import serializers

class ImgViewSet(viewsets.ModelViewSet):
    queryset=models.GalleryDb.objects.all()
    serializer_class=serializers.ImgDataSerializer