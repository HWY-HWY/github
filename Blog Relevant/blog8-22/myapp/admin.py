from django.contrib import admin
from .models import *

# Register your models here.


# 注册模型Article
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'text', 'readnum', 'status')
    actions = ['publish_status', 'withdraw_status']

    # 添加admin动作（发表文章）
    def publish_status(self, request, queryset):
        queryset.update(status='p')
    # 指定后台界面动作的关键词
    publish_status.short_description = "发布文章"

    # 添加admin动作（撤回文章）
    def withdraw_status(self, request, queryset):
        queryset.update(status='w')
    withdraw_status.short_description = '撤回文章'



# 注册模型Read_Num
class Read_NumAdmin(admin.ModelAdmin):
    list_display = ('id', 'read_num_data', 'article')

admin.site.register(Article, ArticleAdmin)
admin.site.register(Read_Num, Read_NumAdmin)
admin.site.register(Test)

