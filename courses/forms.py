from django import forms
from django.forms import SelectMultiple, TextInput, Textarea

from courses.models import Kitap

# class BookCreateForm(forms.Form):
#     title = forms.CharField(
#         label = "Kitap Başlığı",
#         required = True,
#         error_messages = {"required":"Kitap Başlığı girmelisiniz."},
#         widget=forms.TextInput(attrs={"class":"form-control"}))
     
#     description = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control"}))
#     imageUrl = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
#     slug = forms.SlugField(widget=forms.TextInput(attrs={"class":"form-control"}))

class BookCreateForm(forms.ModelForm):
    class Meta:
        model = Kitap
    
        fields = ('title','description','image','slug',)
        labels = {
            'title':"Kitap Başlığı",
            'description':"Kitap Açıklaması"
        }
        widgets = {
            "title": TextInput(attrs={"class":"form-control"}),
            "description": Textarea(attrs={"class":"form-control"}),
            "slug": TextInput(attrs={"class":"form-control"}),
        }
        error_messages = {
            "title": {
                "required":"Kitap Başlığı girmelisiniz.",
                "max_length":"Maksimum 50 karakter girebilirsiniz."
            },
            "description": {
                "required":"Kitap Açıklaması gereklidir."
            }
        }

class BookEditForm(forms.ModelForm):
    class Meta:
        model = Kitap
        fields = ('title','description','image','slug','categories','isActive')
        labels = {
            'title':"Kitap Başlığı",
            'description':"Kitap Açıklaması"
        }
        widgets = {
            "title": TextInput(attrs={"class":"form-control"}),
            "description": Textarea(attrs={"class":"form-control"}),
            "slug": TextInput(attrs={"class":"form-control"}),
            "categories": SelectMultiple(attrs={"class":"form-control"}),
        }
        error_messages = {
            "title": {
                "required":"Kitap Başlığı girmelisiniz.",
                "max_length":"Maksimum 50 karakter girebilirsiniz."
            },
            "description": {
                "required":"Kitap Açıklaması gereklidir."
            }
        }

class UploadForm(forms.Form):
    image = forms.ImageField()