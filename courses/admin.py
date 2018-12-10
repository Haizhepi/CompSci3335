from django.contrib import admin

from .models import Course, Section, Take


class SessionInLine(admin.StackedInline):
    model = Section
    extra = 1


class CourseAdmin(admin.ModelAdmin):
    inlines = [SessionInLine, ]


admin.site.register(Course, CourseAdmin)
admin.site.register(Section)
admin.site.register(Take)
