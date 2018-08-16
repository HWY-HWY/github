from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib import auth
from .models import *
from .forms import *
from Recent_Read.models import Recent_Read
from django.contrib.contenttypes.models import ContentType

# Create your views here.


# 显示文章数据
def show_Articles_data(request):
    data = Article.objects.all()
    # 得到get请求中的页码参数
    page_num = request.GET.get('page', 1)
    # 实例化一个分页器
    paginator = Paginator(data, 8)
    # 通过页码获得对应的文章，可以使用paginator.page， 但是这个方法不能对get获得的数据进行筛选，所以使用get_page
    article_list = paginator.get_page(page_num)
    # 前端页面参数字典
    context = {}
    context['data'] = article_list.object_list
    context['obj'] = article_list
    context['user'] = request.user
    # 判断是否当前页是否是第一页
    if int(article_list.number) == 1:
        # 总页数超过3页
        if (int(article_list.number) + 2) <= paginator.num_pages:
            context["page_num"] = range(int(article_list.number), int(article_list.number) + 3)
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
            context['page_num'] = range(int(article_list.number) - 1, int(article_list.number) + 2)
        elif (int(article_list.number) - 1) <= 0 and (int(article_list.number) + 1) <= paginator.num_pages:
            context['page_num']=range(1, int(article_list.number) + 2)
        else:
            context['page_num']=range(1, int(article_list.number) + 1)
    return render(request, 'index.html', context)


def content(request):
    pk = request.GET.get('pk')
    try:
        # 通过获得get请求中的数据查询文本内容，根据判断长度来确定是否查找到数据（数据是否存在）
        # 存在数据，则在原数据的基础上加1
        articles = Article.objects.get(pk=pk)
        ct = ContentType.objects.get_for_model(Article)
        # 判断用户是否登录，如果已经登录，则实例化一个历史记录并保存生效
        if not request.user.is_anonymous:
            re = Recent_Read(content_type=ct, object_id=pk,user=request.user)
            re.save()
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
        context['pk'] = pk
        context['user'] = request.user
        return render(request, 'content_template.html', context)
    except:
        return HttpResponse('404')


# 用户登录
def login(request):
    if request.method == "GET":
        context = {}
        context['previous_page'] = request.GET.get('from_page', '/index')
        return render(request, 'login.html', context)
    else:
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = authenticate(request, username=username, password=password)
            auth.login(request, user)
            return HttpResponseRedirect(request.GET.get('from_page', '/index'))
        except:
            context = {}
            context['login_info'] = True
            context['previous_page']=request.GET.get('from_page', '/index')
            return render(request, 'login.html', context)


# 用户注销
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(request.GET.get('from_page', '/index'))


# 用户注册
def register(request):
    if request.method == "GET":
        context = {}
        context['previous_page'] = request.GET.get('from_page', '/index')
        return render(request, 'register.html', context)
    else:
        try:
            username = request.POST['username']
            password = request.POST['password']
            # 判断用户名是否存在
            if User.objects.filter(username=username).exists():
                context = {}
                context['register_info'] = True
                context['previous_page']=request.GET.get('from_page', '/index')
                return render(request, 'register.html', context)
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                return HttpResponseRedirect(request.GET.get('from_page', '/index'))
        except:
            return HttpResponse('注册过程异常，请重新注册！')


# Django form表单测试
def loginform(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        # 判断接受的数据是否有效，有效则为True，否则为FALSE（比如输入的是一串空格）
        if login_form.is_valid():
            user = login_form.cleaned_data['user']
            auth.login(request, user)
            return HttpResponseRedirect(request.GET.get('from_page'))
    else:
        # 实例化一个Form表单对象
        login_form = LoginForm()
    context = {}
    # 传递给模板文件
    context['login_form'] = login_form
    return render(request, 'test.html', context)


# 测试用视图函数
def test(request):
    user = request.user
    print(dir(user))
    print(user.is_anonymous)
    return HttpResponse('test')

