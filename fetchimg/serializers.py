from rest_framework import serializers
from .models import GalleryDb

class ImgDataSerializer(serializers.ModelSerializer):
    class Meta:
        model=GalleryDb
        fields='__all__'