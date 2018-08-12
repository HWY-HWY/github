from django.shortcuts import render
from Like.models import LikeAr
from django.contrib.contenttypes.models import ContentType
from django.http import JsonResponse

# Create your views here.


def like_up(request):
    data = {}
    data['status'] = 'SUCCESS'
    data['is_like'] = "ok"
    return JsonResponse(data)
