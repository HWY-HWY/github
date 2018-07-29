from django.db import models

# Create your models here.


# 创建一个文章的模型
class Article(models.Model):
    title = models.CharField(max_length=20)
    author = models.CharField(max_length=10)
    text = models.CharField(max_length=200)
    # 图片上传
    img = models.ImageField(upload_to='image', blank=True)
    # 文件上传
    file_upload = models.FileField(upload_to='file', blank=True)

    def readnum(self):
        try:
            self.read_num_data = self.read_num.read_num_data
            return self.read_num_data
        except:
            return 0

    class Meta:
        ordering = ['-id']


# 创建一个记录阅读数量的模型
class Read_Num(models.Model):
    read_num_data = models.IntegerField()
    article = models.OneToOneField('Article', on_delete=models.DO_NOTHING)
