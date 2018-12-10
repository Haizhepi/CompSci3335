from django.shortcuts import get_object_or_404, render, HttpResponse
from accounts.models import UserProfile
from .models import Course, Section, Take
from .resources import CourseResource


def course_list(request):
    courses = Course.objects.all()
    list_course = []
    profile = UserProfile.objects.get(user=request.user)
    print(profile.grade)
    for course in courses:
        if profile.student_grade in ('4', '5'):
            if course.course_level == '1':
                list_course.append(course)
        elif profile.student_grade in ('6','7', '8'):
            if course.course_level == '2':
                list_course.append(course)
        elif profile.student_grade in ('9','10', '11', '12'):
            if course.course_level == '3':
                list_course.append(course)
        else:
            if course.level == 'U':
                list_course.append(course)

    return render(request, 'courses/course_list.html', {'courses': list_course})


def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)

    return render(request, 'courses/course_detail.html', {'course': course, })


def step_detail(request, course_pk, section_pk):
    section = get_object_or_404(Section, course_id=course_pk, pk=section_pk)
    user_profile = UserProfile.objects.filter(user=request.user).first()
    if Take.objects.filter(user=request.user, section=section) and user_profile.approved_to_register != 'Y':
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