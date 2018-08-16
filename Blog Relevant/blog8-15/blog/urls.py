"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from myapp.views import *
from Recent_Read.views import *
from Run.views import run_img_list
from Ajax.views import *
from Like.views import like_up
from Attitude.views import get_attitude

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', show_Articles_data),
    path('content/', content),
    path('login/', login),
    path('logout/', logout),
    path('register/', register),
    path('loginform/', login),
    path('user_info/', user_info),
    path('test/', test),
    path('run_img_list/', run_img_list),
    path('Ajax/', ajax),
    path('ajax_form/', ajax_form),
    path('ajax_page/', ajax_page),
    path('like_up/', like_up),
    path('get_attitude/', get_attitude),
]

# 配置url 当我们访问 settings.MEDIA_URL中的路径时，static会通过document_root去寻找对应的文件
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
