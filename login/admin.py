from django.contrib import admin

from .models import User, DepartmentPollData

# Register your models here.

# Admin注册用户模型
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'group']
    list_filter = ['group']
    list_display_links = ['username']
    list_per_page = 10

admin.site.register(User, UserAdmin)

class DepartmentPollDataAdmin(admin.ModelAdmin):
    list_display = ['user', 'group']
    list_filter = ['group']
    list_display_links = ['user']
    list_per_page = 10

admin.site.register(DepartmentPollData, DepartmentPollDataAdmin)