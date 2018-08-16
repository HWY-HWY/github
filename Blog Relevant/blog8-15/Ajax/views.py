from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from myapp.models import Article
from django.core.paginator import Paginator

# Create your views here.

i = 1


def ajax(request):
    return render(request, 'Ajax.html')


def ajax_form(request):
    data = {}
    data['status'] = 'SUCCESS'
    data['log_info'] = request.POST['username']
    return JsonResponse(data)


# 使用Ajax实现分页功能
def ajax_page(request):
    ar = Article.objects.all()
    paginator = Paginator(ar, 8)
    context = {}
    # 使得全局变量i可以局部使用
    global i
    if request.method == 'GET':
        # 刷新一次页面后回到最初的数据
        i = 1
        # 返回GET请求的模板页面及数据
        context['content'] = paginator.get_page(1).object_list
        return render(request, 'ajax_page.html', context)
    else:
        i += 1
        # 当每次点击加载更多按钮后会加载下一页的数据并传递给前端页面显示
        ar_list = []
        ar_id = []
        context['content']=paginator.get_page(i).object_list
        for ar in context['content']:
            ar_list.append(ar.title)
            ar_id.append(ar.pk)
        data = {}
        data['status']='SUCCESS'
        data['ar_list']=ar_list
        data['ar_id']=ar_id
        # 判断是否有下一页数据
        if paginator.get_page(i).has_next():
            data['has_next'] = 'ok'
        else:
            data['has_next'] = 'no'
        return JsonResponse(data)

