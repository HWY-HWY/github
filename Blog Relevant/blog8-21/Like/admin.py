from django.contrib import admin
from Like.models import LikeCount, LikeRecord

# Register your models here.


class LikeCountAdmin(admin.ModelAdmin):
    list_display = ('pk', 'content_object', 'like_num')


class LikeRecordAdmin(admin.ModelAdmin):
    list_display = ('pk', 'content_object', 'like_user', 'like_time')


admin.site.register(LikeCount, LikeCountAdmin)
admin.site.register(LikeRecord, LikeRecordAdmin)
