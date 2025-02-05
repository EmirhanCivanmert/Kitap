from django import forms
from pdfconverter.models import DosyaYukle

class UploadForm(forms.ModelForm):
    class Meta:
        model = DosyaYukle
        fields = ('file',)