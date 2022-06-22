from django import forms
from .models import GalleryDb

class ImgForm(forms.ModelForm):
    class Meta:
        model=GalleryDb
        fields='__all__'