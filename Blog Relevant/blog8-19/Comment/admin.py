from django.contrib import admin
from .models import Comment

# Register your models here.


class CommentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'content_object', 'comment_time', 'comment_user', 'comment_text')


admin.site.register(Comment, CommentAdmin)
