from django.db import models
from django.contrib.contenttypes.models import ContentType
from ReadNumber.models import *

# Create your models here.


# 创建一个文章的模型
class Article(models.Model):
    title = models.CharField(max_length=20)
    author = models.CharField(max_length=10)
    text = models.CharField(max_length=200)

    def get_read_num(self):
        try:
            ct = ContentType.objects.get_for_model(Article)
            re = ReadNum.objects.filter(content_type=ct, object_id=self.pk)
            return re[0].read_num
        except:
            return 0


class Diary(models.Model):
    title=models.CharField(max_length=20)
    author=models.CharField(max_length=10)
    text=models.CharField(max_length=200)

    def get_read_num(self):
        try:
            ct = ContentType.objects.get_for_model(Diary)
            re = ReadNum.objects.filter(content_type=ct, object_id=self.pk)
            return re[0].read_num
        except:
            return 0
