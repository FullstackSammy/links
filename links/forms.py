from django import forms
from .models import Link 

class LinkForm(forms.ModelForm):
    # Måste användas när du hämtar data från din model
    class Meta:
        model = Link # Säger vilken model formen ska gå efter.
        fields = ['name', 'url', 'slug'] # Vilka attributes som ska bli fields i din LinkModel.