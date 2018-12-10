from django.contrib import admin
from .models import Application, Parent, School

# Register your models here.
admin.site.register(Application)
admin.site.register(School)
admin.site.register(Parent)

admin.site.site_header = 'UYP staff'
