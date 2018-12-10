from django.contrib import admin

from .models import Course, Step, Section


class StepInline(admin.StackedInline):
    model = Step
    extra = 1


class SessionInLine(admin.StackedInline):
    model = Section
    extra = 1


class CourseAdmin(admin.ModelAdmin):
    inlines = [SessionInLine, StepInline, ]


admin.site.register(Course, CourseAdmin)
admin.site.register(Step)