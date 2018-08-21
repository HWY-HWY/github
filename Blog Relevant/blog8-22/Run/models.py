from django.db import models

# Create your models here.


class Run(models.Model):
    img = models.ImageField(upload_to='./img')
    time = models.DateTimeField(auto_now_add=True)
    is_delete = models.BooleanField(default=False)

    class Meta:
        ordering = ['-time']
