from django.shortcuts import render, HttpResponse
from .models import *

# Create your views here.


# 显示文章数据
def show_Articles_data(request):
    data = Article.objects.all()
    context = {}
    context['data'] = data
    return render(request, 'index.html', context)


# 显示具体内容
def content(request):
    pk = request.GET.get('pk')
    article = Article.objects.get(pk=pk)
    # 得到一个可以实例化ReadNum的模型类
    ct=ContentType.objects.get_for_model(Article)
    try:
        # 查询数据库
        re=ReadNum.objects.get(content_type=ct, object_id=pk)
        # 阅读数量加1
        re.read_num += 1
        re.save()
    except:
        # 没有数据，实例化一个对象，并将阅读数量设置为1
        re = ReadNum(content_type=ct, object_id=pk, read_num=1)
        re.save()
    context = {}
    context['blog'] = article
    return render(request, 'content_template.html', context)
