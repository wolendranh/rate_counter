from django.contrib import admin
from rate.models import StudentGroup, Institute, Subject, Rate

# Register your models here.
admin.site.register([StudentGroup, Institute, Subject, Rate])
