from django.contrib import admin
from .models import Run

# Register your models here.


class RunAdmin(admin.ModelAdmin):
    list_display = ('pk', 'time')


admin.site.register(Run, RunAdmin)
