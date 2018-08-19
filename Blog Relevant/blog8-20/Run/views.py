from django.shortcuts import render
from .models import Run
from django.core.paginator import Paginator

# Create your views here.


def run_img_list(request):
    run_list = Run.objects.filter(is_delete=False)
    # 得到get请求中的页码参数
    page_num = request.GET.get('page', 1)
    # 实例化一个分页器
    paginator = Paginator(run_list, 20)
    # 通过页码获得对应的文章，可以使用paginator.page， 但是这个方法不能对get获得的数据进行筛选，所以使用get_page
    article_list = paginator.get_page(page_num)
    context = {}
    context['run_list'] = article_list
    context['data'] = article_list.object_list
    context['obj'] = article_list
    # 判断是否当前页是否是第一页
    if int(article_list.number) == 1:
        # 总页数超过3页
        if (int(article_list.number) + 2) <= paginator.num_pages:
            context["page_num"]=range(int(article_list.number), int(article_list.number) + 3)
        else:
            context["page_num"]=range(int(article_list.number), int(paginator.num_pages) + 1)
    # 判断是否是最后一页
    elif not article_list.has_next():
        if (int(article_list.number) - 2) > 0:
            context["page_num"]=range(int(article_list.number) - 2, int(article_list.number) + 1)
        else:
            context["page_num"]=range(1, int(article_list.number) + 1)
    else:
        if (int(article_list.number) - 1) > 0 and (int(article_list.number) + 1) <= paginator.num_pages:
            context['page_num']=range(int(article_list.number) - 1, int(article_list.number) + 2)
        elif (int(article_list.number) - 1) <= 0 and (int(article_list.number) + 1) <= paginator.num_pages:
            context['page_num']=range(1, int(article_list.number) + 2)
        else:
            context['page_num']=range(1, int(article_list.number) + 1)
    return render(request, 'run_img_list.html', context)
