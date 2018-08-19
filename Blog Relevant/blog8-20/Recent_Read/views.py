from django.shortcuts import render
from .models import Recent_Read

# Create your views here.


# 用户信息
def user_info(request):
    user = request.user
    if not user.is_anonymous:
        articles = Recent_Read.objects.filter(user=user, is_delete=False)[0:40]
        context = {}
        context['articles'] = articles
        return render(request, 'user_info.html', context)
    else:
        return render(request, 'error.html')