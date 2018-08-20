from django.shortcuts import render, HttpResponseRedirect
from django.contrib.contenttypes.models import ContentType
from django.http import JsonResponse
from .models import LikeCount, LikeRecord

# Create your views here.


# 数据操作成功返回数据方法
def success_response(like_num):
    data = {}
    data['status'] = 'SUCCESS'
    data['like_num'] = like_num
    return JsonResponse(data)


# 数据操作失败返回信息的方法
def error_response(message):
    data = {}
    data['status'] = 'ERROR'
    data['message'] = message
    return JsonResponse(data)


def like_up(request):
    # 得到GET中的数据以及当前用户
    user = request.user
    # 判断用户是否登录
    if not user.is_authenticated:
        return error_response('未登录，不能进行点赞操作')
    content_type = request.GET.get('content_type')
    content_type = ContentType.objects.get(model=content_type)
    object_id = request.GET.get('object_id')
    is_like = request.GET.get('is_like')

    # 创建一个点赞记录
    if is_like == 'true':
        # 进行点赞，即实例化一个点赞记录
        like_record, created = LikeRecord.objects.get_or_create(content_type=content_type, object_id=object_id, like_user=user)
        # 通过created来判断点赞记录是否存在，如果存在则不进行点赞，如果不存在则进行点赞数量加一
        if created:
            # 不存在点赞记录并且已经创建点赞记录，需要将点赞数量加一
            like_count, created = LikeCount.objects.get_or_create(content_type=content_type, object_id=object_id)
            like_count.like_num += 1
            like_count.save()
            return success_response(like_count.like_num)
        else:
            # 已经进行过点赞
            return error_response('已经点赞过')
    else:
        # 取消点赞
        # 先查询数据是否存在，存在则进行取消点赞
        if LikeRecord.objects.filter(content_type=content_type, object_id=object_id, like_user=user).exists():
            # 数据存在，取消点赞
            # 删除点赞记录
            LikeRecord.objects.get(content_type=content_type, object_id=object_id, like_user=user).delete()
            # 判断对应的点赞数量数据是否存在，如果存在则对点赞数量进行减一
            like_count, create = LikeCount.objects.get_or_create(content_type=content_type, object_id=object_id)
            if create:
                # 数据不存在，返回错误信息
                return error_response('数据不存在，不能取消点赞')
            else:
                # 数据存在，对数量进行减一
                like_count.like_num -= 1
                like_count.save()
                return success_response(like_count.like_num)
        else:
            # 数据不存在，不能取消点赞
            return error_response('数据不存在，不能取消点赞')

