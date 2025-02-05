from django.db import models

class DosyaYukle(models.Model):
    file = models.FileField(upload_to='uploads/')
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name
