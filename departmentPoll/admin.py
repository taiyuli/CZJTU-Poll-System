from django.contrib import admin

from .models import WorkGroup

# Register your models here.

admin.site.site_title = "评分系统后台"
admin.site.site_header = "评分系统后台"

# Admin注册分组模型
class WorkGroupAdmin(admin.ModelAdmin):
    list_display = ['groupName', 'groupDirector']
    list_filter = ['groupDirector']
    list_display_links = ['groupName']
    list_per_page = 10

admin.site.register(WorkGroup, WorkGroupAdmin)
