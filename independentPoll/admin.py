from django.contrib import admin

from .models import LeaderModel, LeaderPollDataModel, DepartmentModel, DepartmentPollDataModel

# Register your models here.


class LeaderModelAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['name']
    list_display_links = ['name']
    list_per_page = 10

admin.site.register(LeaderModel, LeaderModelAdmin)


class LeaderPollDataModelAdmin(admin.ModelAdmin):
    list_display = ['leader', 'user']
    list_filter = ['leader', 'user']
    list_per_page = 10

admin.site.register(LeaderPollDataModel, LeaderPollDataModelAdmin)


class DepartmentModelAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['name']
    list_display_links = ['name']
    list_per_page = 10

admin.site.register(DepartmentModel, DepartmentModelAdmin)


class DepartmentPollDataModelAdmin(admin.ModelAdmin):
    list_display = ['department', 'user']
    list_filter = ['department', 'user']
    list_per_page = 10

admin.site.register(DepartmentPollDataModel, DepartmentPollDataModelAdmin)