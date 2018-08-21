from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib import auth
from .models import *
from .forms import *
from Recent_Read.models import Recent_Read
from django.contrib.contenttypes.models import ContentType
from Comment.models import Comment
from Comment.Form.comment_text_form import CommentText
from django.http import JsonResponse
import random
from django.core.mail import send_mail

# Create your views here.


# Ajax请求错误响应方法
def error_response(message):
    data = {}
    data['status'] = 'ERROR'
    data['message'] = message
    return JsonResponse(data)


# Ajax请求成功响应方法
def success_response(previous_page, message):
    data = {}
    data['status'] = 'SUCCESS'
    data['message'] = message
    data['previous_page'] = previous_page
    return JsonResponse(data)


# 得到评论的数据
def get_comment(content_type, object_id):
    content_type = ContentType.objects.get(model=content_type)
    comment_status = Comment.objects.filter(content_type=content_type, object_id=object_id).exists()
    # 有评论数据
    if comment_status:
        return Comment.objects.filter(content_type=content_type, object_id=object_id)
    # 没有评论数据
    else:
        return 'None'


# 显示文章数据
def show_Articles_data(request):
    data = Article.objects.filter(status='p')
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
    # try:
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
        context['log_info'] = request.user.is_authenticated

        # 得到评论数据
        comment_data = get_comment('article', pk)
        context['comment_data'] = comment_data

        # 得到评论表单
        context['comment_form'] = CommentText()

        return render(request, 'content_template.html', context)
    # except:
        return HttpResponse('404')


# 用户登录
def login(request):
    if request.method == "GET":
        context = {}
        context['previous_page'] = request.GET.get('from_page', '/index')
        return render(request, 'login.html', context)
    else:
        username_or_email = request.POST['username_or_email']
        password = request.POST['password']
        previous_page = request.POST['previous_page']
        try:
            # 根据用户名判断用户是否存在
            user = authenticate(request, username=username_or_email, password=password)
            if user is None:
                # user为空，说明以username_or_email为用户名不正确，还需要判断username_or_email是否为邮箱
                # 假定为邮箱，判断该邮箱是否存在，如果存在则取出其用户名进行判断
                if User.objects.filter(email=username_or_email).exists():
                    username = User.objects.get(email=username_or_email).username
                    user = authenticate(request, username=username, password=password)
                    if user is None:
                        # username_or_email为邮箱时也不成立，说明输入的信息错误
                        return error_response('用户名或密码错误！')
                else:
                    # username_or_email为邮箱时也不成立，说明输入的信息错误
                    return error_response('用户名或密码错误！')
            # 该用户存在，进行登录
            auth.login(request, user)
            return success_response(previous_page, '登录成功！')
        except:
            return error_response('登录过程出现错误，请重新登录！')


# 用户注销
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(request.GET.get('from_page', '/index'))


# 用户注册
def register(request):
    # GET请求处理方法
    if request.method == "GET":
        context = {}
        # 得到来源页面
        context['previous_page'] = request.GET.get('from_page', '/index')
        return render(request, 'register.html', context)
    # POST请求处理方法
    else:
        try:
            # 得到用户名和密码
            username = request.POST['username']
            password = request.POST['password']
            # 判断两次输入的密码是否一致
            if not password == request.POST['again_password']:
                return error_response('两次输入的密码不一致！')
            # 判断用户名是否存在
            if User.objects.filter(username=username).exists():
                return error_response('用户名已存在!')
            else:
                # 判断输入的验证码是否正确
                if request.session.get('code') == request.POST['verification_code']:
                    user = User.objects.create_user(username=username, password=password, email=request.POST['email'])
                    user.save()
                    return success_response(request.POST['previous_page'], '注册成功！')
                else:
                    return error_response('验证码错误！')
        # 其余错误
        except:
            return error_response('注册过程异常，请重新注册！')


# 忘记密码对应的处理方法
def forgot_password(request):
    if request.method == 'GET':
        return render(request, 'forgot_password.html')
    else:
        # 得到表单中的数据
        # 邮箱
        email = request.POST['email']
        # 验证码
        verification_code = request.POST['verification_code']
        # 密码
        password = request.POST['password']
        # 确认密码
        again_password = request.POST['again_password']
        # 验证验证码是否正确
        if not verification_code == request.session.get('code'):
            return error_response('验证码错误！')
        # 验证码通过，验证两次的密码是否相同
        if not password == again_password:
            return error_response('两次输入的密码不一致！')
        # 验证码和密码全通过，可以重置密码
        try:
            user = User.objects.get(email=email)
            user.set_password(password)
            user.save()
            # 清除session
            request.session.clear()
            data = {}
            data['status'] = 'SUCCESS'
            data['message'] = '密码修改成功'
            return JsonResponse(data)
        except:
            return error_response('修改密码过程出现错误，请重试！')


# 忘记密码的验证码请求方法
def forgot_code(request):
    # 得到邮箱
    email = request.POST['email']
    # 判断邮箱是否存在
    if not User.objects.filter(email=email).exists():
        return error_response('该邮箱未绑定！')
    # 邮箱存在，发送验证码
    request.session['code'] = generate_verification_code()
    # 发送邮件
    send_mail(
        # 发送邮件的标题
        '黄文杨的个人网站~找回密码验证码~，谢谢使用！',
        # 发送邮件的内容
        request.session.get('code'),
        # 发送者
        '2551628690@qq.com',
        # 接受者
        [email],
        # 发送失败是否返回错误信息
        fail_silently=False,
    )
    data = {}
    data['status'] = 'SUCCESS_CODE'
    return JsonResponse(data)


# 生成验证码请求方法
def get_verification_code(request):
    data = {}
    # 判断邮箱是否已经注册
    if User.objects.filter(email=request.POST['email']).exists():
        return error_response('该邮箱已经注册！')
    data['status'] = 'SUCCESS'
    # 得到随机的四位验证码
    request.session['code'] = generate_verification_code()
    # 发送邮件
    send_mail(
        # 发送邮件的标题
        '黄文杨的个人网站~验证码~，谢谢使用！',
        # 发送邮件的内容
        request.session.get('code'),
        # 发送者
        '2551628690@qq.com',
        # 接受者
        [request.POST['email']],
        # 发送失败是否返回错误信息
        fail_silently=False,
    )
    return JsonResponse(data)


# 得到四位随机验证码
def generate_verification_code():
    code_list = []
    for i in range(2):
        random_num = random.randint(0, 9)
        a = random.randint(97, 122)
        random_uppercase_letter = chr(a)
        code_list.append(str(random_num))
        code_list.append(random_uppercase_letter)
        verification_code = ''.join(code_list)
    return verification_code


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
    print(request.session.get('code'))
    print(user.is_anonymous)
    return HttpResponse('test')

