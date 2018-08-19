from django.shortcuts import render, HttpResponse
from django.core.mail import send_mail

# Create your views here.


def send(request):
    send_mail(
        # 发送邮件的标题
        '黄文杨的个人网站，谢谢使用！',
        # 发送邮件的内容
        'Here is the message.',
        # 发送者
        '2551628690@qq.com',
        # 接受者
        ['1838531437@qq.com', '442276457@qq.com'],
        # 发送失败是否返回错误信息
        fail_silently=False,
    )
    return HttpResponse('发送成功')
