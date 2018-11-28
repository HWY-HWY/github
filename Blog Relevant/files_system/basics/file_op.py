import os

# 删除文件
def file_rm(file_path):
    if file_path == '':
        return 'file_path error'
    try:
        # 将文件备份到回收站
        cp = os.system('cp ' + file_path + ' /Users/hwy/Desktop/回收站')
        # 备份完成后再删除
        re = os.system('rm ' + file_path)
        if re != 0:
            return 'rm error'
        else:
            return 'rm success'
    except:
        return 'rm error'

# 删除文件夹
def dir_rm(file_path):
    if file_path == '':
        return 'file_path error'
    try:
        # 将文件夹备份到回收站
        cp = os.system('cp -r ' + file_path + ' /Users/hwy/Desktop/回收站')
        re = os.system('rm -r ' + file_path)
        if re != 0:
            return 'rm error'
        else:
            return 'rm success'
    except:
        return 'rm error'


# 新建文件夹
def mkdir_file(file_path):
    if file_path == '':
        return 'file_path error'
    try:
        re = os.system('mkdir ' + file_path)
        if re != 0:
            return 'mkdir error'
        else:
            return 'mkdir success'
    except:
        return 'mkdir error'


# 重命名文件
def rename(file_path, name, new_name):
    if file_path == '':
        return 'file_path error'
    try:
        re = os.system('mv ' + file_path + name +  ' ' + file_path + new_name)
        if re != 0:
            return 'rename error'
        else:
            return 'rename success'
    except:
        return 'rename error'

# 重命名文件夹
def rename_dir(file_path, name, new_name):
    if file_path == '':
        return 'file_path error'
    try:
        re = os.system('mv ' + file_path + name +  ' ' + file_path + new_name)
        if re != 0:
            return 'rename error'
        else:
            return 'rename success'
    except:
        return 'rename error'


# 解压文件
def unzip(file_path, sub_path):
    if file_path == '' or sub_path == '':
        return 'file_path or sub_path reeor'
    try:
        re = os.system('unrar x ' + file_path + ' '  + sub_path  + ' -y')
        if re != 0:
            return 'unzip error'
        else:
            return 'unzip success'
    except:
        return 'unzip error'


# 对文件夹进行压缩
def rar(sub_path, file_name, new_name):
    if sub_path == '':
        return 'file path error'
    try:
        print('rar a ' + sub_path + new_name + ' ' + sub_path + file_name)
        re = os.system('rar a ' + sub_path + new_name + ' ' + sub_path + file_name)
        if re != 0:
            return 'rar error'
        else:
            return 'rar success'
    except:
        return 'rar error'


