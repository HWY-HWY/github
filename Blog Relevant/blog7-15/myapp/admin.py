from django.contrib import admin
from .models import *

# Register your models here.


# 注册模型Article
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'text', 'get_read_num')


admin.site.register(Article, ArticleAdmin)
admin.site.register(Diary, ArticleAdmin)
