from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User

# Create your models here.


# 用于记录点赞数量的模型
class LikeCount(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.DO_NOTHING)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    # 用于记录点赞数量的字段
    like_num = models.IntegerField(default=0)


# 用于记录点赞状态的模型
class LikeRecord(models.Model):
    content_type=models.ForeignKey(ContentType, on_delete=models.DO_NOTHING)
    object_id=models.PositiveIntegerField()
    content_object=GenericForeignKey('content_type', 'object_id')
    # 记录点赞的用户
    like_user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    # 记录点赞的时间
    like_time = models.DateTimeField(auto_now_add=True)
