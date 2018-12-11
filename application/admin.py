from django.contrib import admin
from .models import Application, Parent, School

# Register your models here.
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['user', 'application_status',]


admin.site.register(Application, ApplicationAdmin)
admin.site.register(School)
admin.site.register(Parent)

admin.site.site_header = 'UYP staff'
