from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


# Create your models here.

class ReadNum(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.DO_NOTHING)
    object_id = models.PositiveIntegerField()
    read_num = models.IntegerField(default=0)
    # 通过content_type和object_id去实例化一个对象
    content_object = GenericForeignKey('content_type', 'object_id')
