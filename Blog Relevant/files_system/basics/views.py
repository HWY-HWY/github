from django.shortcuts import render, HttpResponse, HttpResponseRedirect
import os
from django.http import StreamingHttpResponse
import base64
import re
from .file_op import file_rm, dir_rm, mkdir_file, rename, unzip, rar
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from django.contrib import auth


# Create your views here.


# 显示基础路径信息
def index(request):
    if request.user.is_anonymous:
        return HttpResponseRedirect('/login')
    # 基本路径
    path = '/Users/hwy/Desktop'
    file_list = os.listdir(path)
    for i in range(0, len(file_list)):
        # 遍历所有的文件，并且判断是否是文件夹
        if os.path.isdir(os.path.join(path, file_list[i])):
            # 是文件夹，加上文件夹的标志，并且拼接完整路径
            file_list[i] = {'states': True, 'url': os.path.join(path, file_list[i]), 'sub_url': file_list[i]}
        else:
            # 判断是否是压缩文件
            if '.rar' in file_list[i]:
                file_list[i] = {'states': False, 'url': os.path.join(path, file_list[i]), 'sub_url': file_list[i], 'is_rar': True}
            else:
                file_list[i] = {'states': False, 'url': os.path.join(path, file_list[i]), 'sub_url': file_list[i], 'is_rar': False}


    context = {}
    context['file_list'] = file_list
    context['num'] = 'test'
    context['path'] = path
    return render(request, 'index.html', context)


# 获得路径打开文件夹
def open_folder(request):
    if request.user.is_anonymous:
        return HttpResponseRedirect('/login')
    if request.method == 'GET':
        path = request.GET.get('url', '')
        if path == '':
            return HttpResponse('error')
        history_url = path.split('/')[4:]
        # 再次判断该路径是否是文件夹
        if not os.path.isdir(path):
            return HttpResponse('is not folder')
        # 确定是文件夹，打开文件
        # 判断当前路径是否在根目录之下，不是则不能打开
        re1_str = '/Users/hwy/(Desktop[\s\S]*?)'
        result = re.findall(re1_str, path)
        # 判断该路径是不是回收站路径或子路径
        if not '/Users/hwy/Desktop/回收站' in path:
            if result == []:
                return HttpResponse('访问路径不合法')
        file_list = os.listdir(path)
        for i in range(0, len(file_list)):
        # 遍历所有的文件，并且判断是否是文件夹
            if os.path.isdir(os.path.join(path, file_list[i])):
                # 是文件夹，加上文件夹的标志，并且拼接完整路径
                file_list[i] = {'states': True, 'url': os.path.join(path, file_list[i]), 'sub_url': file_list[i]}
            else:
                # 判断是否是压缩文件
                if '.rar' in file_list[i]:
                    file_list[i] = {'states': False, 'url': os.path.join(path, file_list[i]), 'sub_url': file_list[i], 'is_rar': True}
                else:
                    file_list[i] = {'states': False, 'url': os.path.join(path, file_list[i]), 'sub_url': file_list[i], 'is_rar': False}


        context = {}
        context['file_list'] = file_list
        context['path'] = path
        context['history_url'] = history_url
        return render(request, 'index.html', context)

    else:
        return HttpResponse('is not GET request')


# 下载文件
def content(request):
    if request.user.is_anonymous:
        return HttpResponseRedirect('/login')
    if request.method == 'GET':
        path = request.GET.get('url', '')
        if path == '':
            return HttpResponse('error')
        # 再次判断路径是否为文件
        try:
            # 获得文件的后缀名，判断是否是图片格式，如果是图片，则将其转化为base64
            if (os.path.splitext(path)[-1]) in  ['.jpg', '.png', '.jpeg', '.bmp', '.PNG', '.ico']:
                with open(path, "rb") as f:
                    # b64encode是编码，b64decode是解码
                    base64_data = base64.b64encode(f.read())
                context = {}
                context['img_url'] = str(base64_data)[2:-1]
                return render(request, 'img.html', context)
            with open(path, 'r') as f:
                result = f.readlines()
            text = ''
            for line in result:
                text += line
            context = {}
            context['text'] = text
        except:
            return HttpResponse('无法打开文件')
        return render(request, 'content.html', context)
    else:
        return HttpResponse('is not GET request')


def download(request):
    if request.user.is_anonymous:
        return HttpResponseRedirect('/login')
    def file_iterator(file_name, chunk_size=512):
        with open(file_name, 'rb') as f:
            while True:
                c = f.read(chunk_size)
                if c:
                    yield c
                else:
                    break
    the_file_name = request.GET.get('url')
    response = StreamingHttpResponse(file_iterator(the_file_name))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(the_file_name)
    return response



# 根据关键字查询路径并且跳转到指定路径
def jump(request):
    if request.user.is_anonymous:
        return HttpResponseRedirect('/login')
    if request.method == 'GET':
        keywords = request.GET.get('keywords', '')
        if keywords == '':
            return HttpResponse('data error')
        sum_path = request.GET.get('path', '')
        if sum_path == '':
            return HttpResponse('data error')
        re1_str = '([\s\S]*?' + keywords + ')'
        result = re.findall(re1_str, sum_path)[0]
        return HttpResponseRedirect('/open_folder?url=' + result)
    else:
        return HttpResponse('is not GET request')


# 文件删除
def rm_file(request):
    if request.user.is_anonymous:
        return HttpResponseRedirect('/login')
    if request.method == 'GET':
        # 获得文件路径
        file_path = request.GET.get('url', '')
        if file_path == '':
            return HttpResponse('file_path is none')
        re = file_rm(file_path)
        return HttpResponse(re)
    else:
        return HttpResponse('is not GET request')
    pass


# 利用ajax实现文件删除
def rm_file_ajax(request):
    if request.user.is_anonymous:
        return HttpResponseRedirect('/login')
    if request.method == 'GET':
        # 得到文件路径
        file_path = request.GET.get('path', '')
        print(file_path)
        if file_path == '':
            return HttpResponse('file_path error')
        # 判断文件是文件还是文件夹
        if os.path.isdir(file_path):
            # 是文件夹，使用删除文件夹的方式删除文件夹
            re = dir_rm(file_path)
            if re != 'rm success':
                data = {}
                data['status'] = 'error'
                data['message'] = re
                return JsonResponse(data)
            data = {}
            data['status'] = 'success'
            data['message'] = re
            return JsonResponse(data)

        # 删除文件
        re = file_rm(file_path)
        if re != 'rm success':
            data = {}
            data['status'] = 'error'
            data['message'] = re
            return JsonResponse(data)
        data = {}
        data['status'] = 'success'
        data['message'] = re
        return JsonResponse(data)
    else:
        return HttpResponse('is not GET reuest')


# 新建文件夹
def mkdir(request):
    if request.user.is_anonymous:
        return HttpResponseRedirect('/login')
    if request.method == 'GET':
        # 获得创建文件夹的路径
        path = request.GET.get('path', '')
        print(path)
        # 获得文件夹名称
        file_name = request.GET.get('file_name', '')
        if file_name == '':
            data = {}
            data['status'] = 'error'
            data['message'] = '文件夹名称不能为空'
            return JsonResponse(data)
        if path == '':
            data = {}
            data['status'] = 'error'
            data['message'] = 'error'
            return JsonResponse(data)
        # 路径拼接，得到具体文件夹路径
        file_path = os.path.join(path, file_name)
        # 创建文件夹
        re = mkdir_file(file_path)
        if re != 'mkdir success':
            data = {}
            data['status'] = 'error'
            data['message'] = re
            return JsonResponse(data)

        data = {}
        data['status'] = 'success'
        data['message'] = re
        return JsonResponse(data)

    else:
        return HttpResponse('is not GET request')


# 返回上一级
def go_back(request):
    if request.user.is_anonymous:
        return HttpResponseRedirect('/login')
    # 得到当前所在的路径
    path = request.GET.get('path', '')
    if path == '':
        return HttpResponse('file path error')
    # 对路径进行分割，在去掉最后的部分获得上一级的路径
    result = path.split('/')
    f = ''
    for i in range(1, len(result)-1):
        print(result[i])
        f += '/' + result[i]
    result = f
    return HttpResponseRedirect('/open_folder?url=' + result)

# 文件重命名
def file_rename(request):
    if request.user.is_anonymous:
        return HttpResponseRedirect('/login')
    path = request.GET.get('path', '')
    name = request.GET.get('name', '')
    new_name = request.GET.get('new_name', '')
    if new_name == '':
        data = {}
        data['status'] = 'error'
        data['message'] = '文件名不能为空'
        return JsonResponse(data)
    if (path == '') or (name == ''):
        return 'file path is none'
    # 判断是否为文件夹
    if os.path.isdir(path):
        re1_str = '([\s\S]*?)' + name
        path = re.findall(re1_str, path)[0]
        # 判断新名称是否存在，如果存在则不能重命名
        name_list = []
        file_list = os.listdir(path)
        for i in range(0, len(file_list)):
            # 遍历所有的文件，并且判断是否是文件夹
            if os.path.isdir(os.path.join(path, file_list[i])):
            # 是文件夹
                name_list.append(file_list[i])
        if new_name in name_list:
            data = {}
            data['status'] = 'error'
            data['message'] = '文件夹已经存在'
            return JsonResponse(data)
        # 修改文件夹名
        result = rename(path, name, new_name)
        if result != 'rename success':
            data = {}
            data['status'] = 'error'
            data['message'] = result
            return JsonResponse(data)
        data = {}
        data['status'] = 'success'
        data['message'] = result
        return JsonResponse(data)

   # 对路径进行剪切
    re1_str = '([\s\S]*?)' + name
    path = re.findall(re1_str, path)[0]
    print(path, name, new_name)
    # 判断新名称是否存在，如果存在则不能重命名
    name_list = []
    file_list = os.listdir(path)
    for i in range(0, len(file_list)):
        # 遍历所有的文件，并且判断是否是文件夹
        if not os.path.isdir(os.path.join(path, file_list[i])):
            # 是文件
            name_list.append(file_list[i])
    if new_name in name_list:
        data = {}
        data['status'] = 'error'
        data['message'] = '文件名已经存在'
        return JsonResponse(data)

    result = rename(path, name, new_name)
    if result != 'rename success':
            data = {}
            data['status'] = 'error'
            data['message'] = result
            return JsonResponse(data)
    data = {}
    data['status'] = 'success'
    data['message'] = result
    return JsonResponse(data)

def test(request):
    if request.user.is_anonymous:
        return HttpResponseRedirect('/login')
    return render(request, 'test.html')


def upload(request):
    if request.user.is_anonymous:
        return HttpResponseRedirect('/login')
    # 处理分片文件的接收与保存
    if request.method == 'POST':
        my_file = request.FILES.get('file')
        if not my_file:
            return HttpResponse('文件不存在')
        task = request.POST.get('task_id')  # 获取文件唯一标识符
        # 获取当前路径
        path = request.POST.get('path', '')
        print(path)
        chunk = request.POST.get('chunk', 0)  # 获取该分片在所有分片中的序号
        filename = '%s%s' % (task, chunk)  # 构成该分片唯一标识符，也是保存的文件名
        with open(path + '/' + filename, 'wb') as f:
            f.write(my_file.read())
    return render(request, 'upload.html')

def upload_success(request):
    if request.user.is_anonymous:
        return HttpResponseRedirect('/login')
    # 小文件传输成功后，前端会自动发起请求到此函数，将小文件合并为大文件，并删除缓存的小文件
    target_filename = request.GET.get('filename')
    task = request.GET.get('task_id') # 获取文件的唯一标识符
    # 获得当前路径
    path = request.GET.get('path')
    print(path)
    chunk = 0
    with open(path + '/%s' % target_filename, 'wb') as target_file:
        while True:
            try:
                filename = path + '/%s%d' % (task, chunk)
                print(filename)
                source_file = open(filename, 'rb')  # 按序打开每个分片
                target_file.write(source_file.read())  # 读取分片内容写入新文件
                source_file.close()
            except IOError:
                break
            chunk += 1
            os.remove(filename)  # 删除该分片，节约空间
    return render(request, 'upload.html')


# 解压文件
def file_unzip(request):
    if request.user.is_anonymous:
        return HttpResponseRedirect('/login')
    data= {}
    # 得到当前路径
    path = request.GET.get('url', '')
    if path == '':
        data['status'] = 'error'
        data['message'] = 'file path error'
        return JsonResponse(data)
    # 得到该文件的名称
    file_name = request.GET.get('file_name', '')
    if file_name == '':
        data['status'] = 'error'
        data['message'] = 'file name error'
        return JsonResponse(data)
    # 利用正则表达式进行路径切割
    re1_str = '([\s\S]*?)' + file_name
    sub_path = re.findall(re1_str, path)[0]
    result = unzip(path, sub_path)
    if result != 'unzip success':
        data['status'] = 'error'
        data['message'] = 'unzip error'
        return JsonResponse(data)
    data['status'] = 'success'
    data['message'] = '解压完成'
    return JsonResponse(data)


# 对文件夹进行压缩
def file_rar(request):
    if request.user.is_anonymous:
        return HttpResponseRedirect('/login')
    data = {}
    # 得到文件夹路径
    file_path = request.GET.get('path', '')
    # 得到文件夹名称
    file_name = request.GET.get('file_name', '')
    # 得到新的文件名
    new_name = request.GET.get('new_name', '')
    if file_path == '' or file_name == '':
        data['status'] = 'error'
        data['message'] = 'file path or file name is none'
        return JsonResponse(data)
    if new_name == '':
        data['status'] = 'error'
        data['message'] = '文件名称不能为空'
        return JsonResponse(data)
    # 对文件夹路径进行修剪，以获得根目录
    re1_str = '([\s\S]*?)' + file_name
    sub_path = re.findall(re1_str, file_path)[0]
    print(sub_path, file_name, new_name)
    result = rar(sub_path, file_name, new_name)
    if result != 'rar success':
        data['status'] = 'error'
        data['message'] = 'rar error'
        return JsonResponse(data)
    data['status'] = 'success'
    data['message'] = '压缩完成'
    return JsonResponse(data)


# 登陆
def login(request):
    if request.method == 'POST':
        username = 'hwy'
        password = request.POST.get('password', '')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect('/Load')
        else:
            return HttpResponseRedirect('/login')
    return render(request, 'login.html')

# 加载页面
def Load(request):
    if request.user.is_anonymous:
        return HttpResponseRedirect('/login')
    return render(request, 'Load.html')
