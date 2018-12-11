from django.shortcuts import get_object_or_404, render, HttpResponse, redirect
from accounts.models import UserProfile
from .models import Course, Section, Take
from .resources import CourseResource
from application.models import Application


def course_list(request):

    if UserProfile.objects.filter(user=request.user):
        applist = Application.objects.filter(user=request.user)
        flag = False
        for app in applist:
            if app.application_status == 'A':
                flag = True
        prof = UserProfile.objects.get(user=request.user)
        if flag:
            prof.approved_to_register = 'Y'
            prof.save()
        if prof.approved_to_register:
            courses = Course.objects.all()
            list_course = []
            profile = UserProfile.objects.get(user=request.user)
            print(profile.grade)
            for course in courses:
                if profile.student_grade in ('1', '2'):
                    if course.course_level in ('1', ):
                        list_course.append(course)
                elif profile.student_grade in ('3', '4', '5'):
                    if course.course_level in ('1', '2'):
                        list_course.append(course)
                elif profile.student_grade in ('6','7', '8', '9'):
                    if course.course_level in ('1', '2', '3'):
                        list_course.append(course)
                else:
                    if course.level == 'U':
                        list_course.append(course)
        else:
            return render(request, 'courses/profile_incomplete.html', {'message': 'you must finish your application'})

        return render(request, 'courses/course_list.html', {'courses': list_course})
    else:
        return render(request, 'courses/profile_incomplete.html', {'message': 'you must finish your user profile'})


def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)

    return render(request, 'courses/course_detail.html', {'course': course, })


def step_detail(request, course_pk, section_pk):
    section = get_object_or_404(Section, course_id=course_pk, pk=section_pk)
    user_profile = UserProfile.objects.filter(user=request.user).first()
    if Take.objects.filter(user=request.user, section=section) or user_profile.approved_to_register != 'Y':
        print('exist')
        return render(request, 'courses/reg_failed.html', {'section': section})
    else:
        section.capacity = section.capacity - 1
        section.save()
        Take.objects.create(user=request.user, section=section).save()

    return render(request, 'courses/step_detail.html', {'section': section})


def my_sections(request):
    my_courses = Take.objects.filter(user=request.user)
    return render(request, 'courses/my_course.html', {'courses': my_courses})


def exportCourse(request):
    course_rec = CourseResource()
    dataset = course_rec.export()
    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="courses.csv"'
    return response