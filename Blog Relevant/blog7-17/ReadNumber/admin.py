from django.contrib import admin
from .models import ReadNum

# Register your models here.


class ReadNumAdmin(admin.ModelAdmin):
    list_display = ('pk', 'content_object')


admin.site.register(ReadNum, ReadNumAdmin)
