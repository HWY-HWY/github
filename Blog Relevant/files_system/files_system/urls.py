"""files_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from basics.views import index, open_folder, download, content, jump, rm_file, rm_file_ajax, mkdir, go_back, file_rename, test, upload, upload_success, file_unzip, file_rar, login, Load
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('open_folder/', open_folder),
    path('download/', download),
    path('content/', content),
    path('jump/', jump),
    path('rm_file/', rm_file),
    path('rm_file_ajax', rm_file_ajax),
    path('mkdir/', mkdir),
    path('go_back/', go_back),
    path('file_rename/', file_rename),
    path('test/', test),
    path('upload/', upload),
    path('upload/success/', upload_success),
    path('file_unzip/', file_unzip),
    path('file_rar/', file_rar),
    path('login/', login),
    path('Load/', Load),
]
