from django.contrib import admin
from .models import AttitudeCount, AttitudeRecord

# Register your models here.


class AttitudeCountAdmin(admin.ModelAdmin):
    list_display = ('pk', 'content_object', 'attitude_flower_num', 'attitude_handshake_num', 'attitude_pass_num', 'attitude_shocking_num', 'attitude_egg_num')


class AttitudeRecordAdmin(admin.ModelAdmin):
    list_display = ('pk', 'content_object', 'attitude_type', 'attitude_user', 'attitude_time')


admin.site.register(AttitudeCount, AttitudeCountAdmin)
admin.site.register(AttitudeRecord, AttitudeRecordAdmin)
