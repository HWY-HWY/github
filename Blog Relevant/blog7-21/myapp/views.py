from django.shortcuts import render, HttpResponse
from .models import *

# Create your views here.


# 显示文章数据
def show_Articles_data(request):
    data = Article.objects.all()
    context = {}
    context['data'] = data
    return render(request, 'index.html', context)


def content(request):
    pk = request.GET.get('pk')
    try:
        # 通过获得get请求中的数据查询文本内容，根据判断长度来确定是否查找到数据（数据是否存在）
        # 存在数据，则在原数据的基础上加1
        articles=Article.objects.get(pk=pk)
        if Read_Num.objects.filter(article=articles).count():
            articles.read_num.read_num_data += 1
            articles.read_num.save()
            # 不存在数据，创建对象，并且使阅读数设置为0
        else:
            readnum = Read_Num()
            readnum.article = articles
            readnum.read_num_data = 1
            readnum.save()
        text = articles.text
        context = {}
        context['text'] = text
        return render(request, 'content_template.html', context)
    except:
        return HttpResponse('404')