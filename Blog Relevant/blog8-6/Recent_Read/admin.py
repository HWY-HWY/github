from django.contrib import admin
from .models import Recent_Read

# Register your models here.


class Recent_ReadAdmin(admin.ModelAdmin):
    list_display = ('content_object', 'Read_time', 'user')


admin.site.register(Recent_Read, Recent_ReadAdmin)