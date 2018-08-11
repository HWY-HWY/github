from django.contrib import admin
from .models import *

# Register your models here.


# 注册模型Article
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'text', 'readnum')


# 注册模型Read_Num
class Read_NumAdmin(admin.ModelAdmin):
    list_display = ('id', 'read_num_data', 'article')

admin.site.register(Article, ArticleAdmin)
admin.site.register(Read_Num, Read_NumAdmin)
admin.site.register(Test)
