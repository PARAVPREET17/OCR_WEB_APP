from django import forms
from .models import Ocr,Contact


class ImageUpload(forms.ModelForm):
    class Meta:
        model = Ocr
        fields = ['image']


class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields=['name', 'email', 'message']
