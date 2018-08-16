# -*- coding: utf-8 -*-
# @File  : get_like_num.py
# @Author: 一稚杨
# @Date  : 2018/8/14/014
# @Desc  : 通过传递过来的类型、相关参数得到对应的点赞数量并返回

from Like.models import LikeCount, LikeRecord
from django import template
from django.contrib.contenttypes.models import ContentType

register = template.Library()


# 得到点赞数量
@register.simple_tag
def get_like_num(content_type, object_id):
    content_type = ContentType.objects.get(model=content_type)
    like_num, create = LikeCount.objects.get_or_create(content_type=content_type, object_id=object_id)
    like_num = like_num.like_num
    return like_num


# 判断当前用户对当前文章是否点赞
@register.simple_tag
def get_like_record(content_type, object_id, user):
    # 判断是否登录，没有登录直接返回空
    if not user.is_authenticated:
        return ''
    content_type = ContentType.objects.get(model=content_type)
    if LikeRecord.objects.filter(content_type=content_type, object_id=object_id, like_user=user).exists():
        # 存在点赞记录， 返回active
        return 'active'
    else:
        return ''
