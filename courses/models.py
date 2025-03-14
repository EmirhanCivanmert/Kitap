from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField

class Category(models.Model):
    name = models.CharField(max_length=40, null=True, blank=True)
    slug = models.SlugField(default="", null=False, unique=True, db_index=True, max_length=50)
    def __str__(self):
        return f"{self.name}"

class Kitap(models.Model):
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=500, default="")
    description = RichTextField()
    image = models.ImageField(upload_to="images", default="")
    date = models.DateField(auto_now=True)
    isActive = models.BooleanField(default=False)
    isHome = models.BooleanField(default=False)
    slug = models.SlugField(default="",blank=True, null=False,unique=True, db_index=True)
    categories = models.ManyToManyField(Category, related_name="books")
    summary = models.CharField(max_length=10000, null=True)

    hikaye_kitap = models.ManyToManyField("self", blank=True)

    def __str__(self):
        return f"{self.title}"
    
class Slider(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images")
    is_active = models.BooleanField(default=False)
    book = models.ForeignKey(Kitap, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.title}"
    
class UploadModel(models.Model):
    image = models.ImageField(upload_to="images")