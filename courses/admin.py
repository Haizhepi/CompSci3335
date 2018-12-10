from django.contrib import admin
import csv, decimal
from django.shortcuts import HttpResponse
from .models import Course, Section, Take
from .resources import CourseResource


class SessionInLine(admin.StackedInline):
    model = Section
    extra = 1


def export_courses(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="courses.csv"'
    writer = csv.writer(response)
    writer.writerow(['level', 'instructor', 'created at', 'title', 'description'])
    books = queryset.values_list('course_level', 'instructor', 'created_at', 'title', 'description')
    for book in books:
        writer.writerow(book)
    return response


export_courses.short_description = 'Export to csv'


class CourseAdmin(admin.ModelAdmin):
    list_display = ['course_level', 'instructor', 'created_at', 'title']
    inlines = [SessionInLine, ]
    actions = [export_courses, ]


def export_section(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="sections.csv"'
    writer = csv.writer(response)
    writer.writerow(['capacity', 'course', 'session', 'time'])
    books = queryset.values_list('capacity', 'course', 'session', 'section_time')
    for book in books:
        writer.writerow(book)
    return response


export_section.short_description = 'Export to csv'


class SectionAdmin(admin.ModelAdmin):
    list_display = ['capacity', 'course', 'session', 'section_time']
    actions = [export_section, ]


def export_take(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="takes.csv"'
    writer = csv.writer(response)
    writer.writerow(['user', 'section'])
    books = queryset.values_list('user', 'section')
    for book in books:
        writer.writerow(book)
    return response


export_take.short_description = 'Export to csv'


class TakeAdmin(admin.ModelAdmin):
    list_display = ['user', 'section']
    actions = [export_take, ]


admin.site.register(Course, CourseAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(Take, TakeAdmin)
