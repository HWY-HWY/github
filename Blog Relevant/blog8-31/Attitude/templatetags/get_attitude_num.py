# -*- coding: utf-8 -*-
# @File  : get_attitude_num.py
# @Author: 一稚杨
# @Date  : 2018/8/15/015
# @Desc  :

from Attitude.models import AttitudeCount, AttitudeRecord
from django import template
from django.contrib.contenttypes.models import ContentType


register = template.Library()


# 对表态数据进行判断，如果表态数量大于5则返回5，以限制表态的高度
def limit_attitude_data(attitude_type, attitude_num):
    if attitude_type == 'flower':
        if attitude_num.attitude_flower_num <= 5:
            return attitude_num.attitude_flower_num
        else:
            return 5
    elif attitude_type == 'handshake':
        if attitude_num.attitude_handshake_num <= 5:
            return attitude_num.attitude_handshake_num
        else:
            return 5
    elif attitude_type == 'pass':
        if attitude_num.attitude_pass_num <= 5:
            return attitude_num.attitude_pass_num
        else:
            return 5
    elif attitude_type == 'shocking':
        if attitude_num.attitude_shocking_num <= 5:
            return attitude_num.attitude_shocking_num
        else:
            return 5
    elif attitude_type == 'egg':
        if attitude_num.attitude_egg_num <= 5:
            return attitude_num.attitude_egg_num
        else:
            return 5
    else:
        return 0


# 得到文章的表态的数据，用于表态数据的显示
@register.simple_tag
def get_attitude_num(content_type, object_id, attitude_type):
    content_type = ContentType.objects.get(model=content_type)
    attitude_num, create = AttitudeCount.objects.get_or_create(content_type=content_type, object_id=object_id)
    return {
        'flower': attitude_num.attitude_flower_num,
        'handshake': attitude_num.attitude_handshake_num,
        'pass': attitude_num.attitude_pass_num,
        'shocking': attitude_num.attitude_shocking_num,
        'egg': attitude_num.attitude_egg_num,
    }.get(attitude_type, 'error')


# 得到文章的表态的数据，用于表态数据的高度显示
@register.simple_tag
def get_attitude_num_height(content_type, object_id, attitude_type):
    content_type = ContentType.objects.get(model=content_type)
    attitude_num, create = AttitudeCount.objects.get_or_create(content_type=content_type, object_id=object_id)
    return {
        'flower': limit_attitude_data('flower', attitude_num),
        'handshake': limit_attitude_data('handshake', attitude_num),
        'pass': limit_attitude_data('pass', attitude_num),
        'shocking': limit_attitude_data('shocking', attitude_num),
        'egg': limit_attitude_data('egg', attitude_num),
    }.get(attitude_type, 'error')


# 判断当前用户对当前文章是否点赞
@register.simple_tag
def get_attitude_record(content_type, object_id, user, attitude_type):
    # 判断是否登录，没有登录直接返回空
    if not user.is_authenticated:
        return ''
    content_type = ContentType.objects.get(model=content_type)
    if AttitudeRecord.objects.filter(content_type=content_type, object_id=object_id, attitude_user=user, attitude_type=attitude_type).exists():
        # 存在点赞记录， 返回active
        return 'active'
    else:
        return ''




