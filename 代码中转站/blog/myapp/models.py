from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.


class books(models.Model):
    title = models.CharField(max_length=20)
    content = RichTextUploadingField()
