from django.contrib import admin
from .models import StudentGroup, Institute, Subject, Rate


class InstituteModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'site_id']
    list_display_links = ['name']


class StudentGroupModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'site_id', 'institute']
    list_display_links = ['name']


class SubjectModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'group']
    list_display_links = ['name']


# Register your models here.
admin.site.register(Institute, InstituteModelAdmin)
admin.site.register(StudentGroup, StudentGroupModelAdmin)
admin.site.register(Subject, SubjectModelAdmin)


