from django.db import models
from django.contrib.contenttypes.models import ContentType
from ReadNumber.models import *
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.


# 创建一个文章的模型
class Article(models.Model):
    title = models.CharField(max_length=20)
    author = models.CharField(max_length=10)
    text = RichTextUploadingField(default='<h3>类别</h3><h4>标题</h4><hr /> \
                                          <h4>概要</h4> <ul><li>概要内容</li></ul><h4>小标题1</h4><ul><li>小标题1内容</li></ul>')

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
    text=RichTextUploadingField()

    def get_read_num(self):
        try:
            ct = ContentType.objects.get_for_model(Diary)
            re = ReadNum.objects.filter(content_type=ct, object_id=self.pk)
            return re[0].read_num
        except:
            return 0
