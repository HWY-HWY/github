from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User

# Create your models here.


# 记录某篇文章用户的发表态度的记录
class AttitudeRecord(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.DO_NOTHING)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    # 创建一个记录态度类型的字段，默认创建的态度为applause（鼓掌）
    attitude_type = models.TextField(default='applause')
    # 记录发表态度的用户
    attitude_user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    # 记录发表态度的时间
    attitude_time = models.DateTimeField(auto_now_add=True)


# 记录某篇文章用户的发表态度的数量
class AttitudeCount(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.DO_NOTHING)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    # 记录鲜花的数量
    attitude_flower_num = models.IntegerField(default=0)
    # 记录握手的数量
    attitude_handshake_num = models.IntegerField(default=0)
    # 记录路过的数量
    attitude_pass_num = models.IntegerField(default=0)
    # 记录雷人的数量
    attitude_shocking_num = models.IntegerField(default=0)
    # 记录鸡蛋的数量
    attitude_egg_num = models.IntegerField(default=0)

