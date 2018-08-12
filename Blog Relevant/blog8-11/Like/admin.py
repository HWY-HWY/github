from django.contrib import admin
from Like.models import LikeAr

# Register your models here.


class LikeArAdmin(admin.ModelAdmin):
    list_display = ('user', 'Read_time', 'is_like', 'content_object')


admin.site.register(LikeAr, LikeArAdmin)
