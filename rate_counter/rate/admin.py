from django.contrib import admin
from .models import StudentGroup, Institute, Subject, TableRow, Table


class InstituteModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'site_id']
    list_display_links = ['name']
    search_fields = ['name', 'site_id']


class StudentGroupModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'site_id', 'institute']
    list_display_links = ['name']
    search_fields = ['name', 'site_id']


class SubjectModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'group']
    list_display_links = ['name']
    search_fields = ['name']


class TableModelAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']
    search_fields = ['name']


class TableRowModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'point', 'coefficient']
    list_display_links = ['name']
    search_fields = ['name']


# Register your models here.
admin.site.register(Institute, InstituteModelAdmin)
admin.site.register(StudentGroup, StudentGroupModelAdmin)
admin.site.register(Subject, SubjectModelAdmin)
admin.site.register(Table, TableModelAdmin)
admin.site.register(TableRow, TableRowModelAdmin)



