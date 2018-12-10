from django.contrib import admin
from accounts.models import UserProfile
import csv, decimal
from django.shortcuts import HttpResponse


# Register your models here.
def export_profile(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="profiles.csv"'
    writer = csv.writer(response)
    writer.writerow(['user', 'middle', 'suffix','address1',
                     'address2', 'city', 'state', 'zip', 'phone', 'grad_year',
                     'birth_date', 'student_grade', 'student_status', 'accepted_to_GT_program',
                     'english_learn', 'approved_to_register'])
    books = queryset.values_list('user', 'middle', 'suffix','address1',
                     'address2', 'city', 'state', 'zip', 'phone', 'grad_year',
                     'birth_date', 'student_grade', 'student_status', 'accepted_to_GT_program',
                     'english_learn', 'approved_to_register')
    for book in books:
        writer.writerow(book)
    return response


export_profile.short_description = 'Export to csv'


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', ]
    actions = [export_profile, ]


admin.site.register(UserProfile, ProfileAdmin)