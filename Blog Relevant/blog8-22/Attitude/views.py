from django.shortcuts import render
from django.http import JsonResponse
from .models import AttitudeRecord, AttitudeCount
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User

# Create your views here.


# 数据操作成功返回数据方法
def success_response(attitude_type, attitude_num):
    data = {}
    data['status'] = 'SUCCESS'
    data['attitude_num'] = attitude_num
    data['attitude_type'] = attitude_type
    return JsonResponse(data)


# 数据操作失败返回信息的方法
def error_response(message):
    data = {}
    data['status'] = 'ERROR'
    data['message'] = message
    return JsonResponse(data)


# 返回提示信息
def message_response(message):
    data = {}
    data['status'] = 'message'
    data['message'] = message
    return JsonResponse(data)


# 自定义的switch方法
def add_attitude_num(attitude_type, attitude_count):
    print(attitude_type)
    if attitude_type == 'flower':
        attitude_count.attitude_flower_num += 1
        attitude_count.save()
        return attitude_count.attitude_flower_num
    elif attitude_type == 'handshake':
        attitude_count.attitude_handshake_num += 1
        attitude_count.save()
        return attitude_count.attitude_handshake_num
    elif attitude_type == 'shocking':
        attitude_count.attitude_shocking_num += 1
        attitude_count.save()
        return attitude_count.attitude_shocking_num
    elif attitude_type == 'pass':
        attitude_count.attitude_pass_num += 1
        attitude_count.save()
        return attitude_count.attitude_pass_num
    elif attitude_type == 'egg':
        attitude_count.attitude_egg_num += 1
        attitude_count.save()
        return attitude_count.attitude_egg_num
    else:
        return error_response('数据错误')


def get_attitude(request):
    # 得到GET请求发送过来的数据
    attitude_type = request.GET.get('attitude_type')
    if not attitude_type in ('flower', 'handshake', 'shocking', 'pass', 'egg'):
        return error_response('只能发表鲜花、握手、路过、雷人、鸡蛋态度')
    user = request.user
    if not user.is_authenticated:
        return error_response('未登录，不能发表态度')
    content_type = request.GET.get('content_type')
    content_type = ContentType.objects.get(model=content_type)
    object_id = request.GET.get('object_id')
    # 如果对该篇文章已经表过态了则不能进行表态
    if AttitudeRecord.objects.filter(attitude_user=user, content_type=content_type, object_id=object_id).exists():
        return message_response('你已经表过态了')
    attitude_record, create = AttitudeRecord.objects.get_or_create(content_type=content_type, object_id=object_id, attitude_type=attitude_type, attitude_user=user)
    if create:
        # 该用户对该文章还没有表过态，创建对应的数据
        attitude_count, create = AttitudeCount.objects.get_or_create(content_type=content_type, object_id=object_id)
        attitude_num = add_attitude_num(attitude_type, attitude_count)
        return success_response(attitude_type, attitude_num)
    else:
        return message_response('你已经表过态了')
    return success_response()

