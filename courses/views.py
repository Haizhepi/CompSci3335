from django.shortcuts import get_object_or_404, render
from accounts.models import UserProfile
from .models import Course, Section, Take


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


# def section_detail(request, pk):                            ##############'section':section
#     section = get_object_or_404(Section, pk=pk)     section = get_object_or_404(Section, pk=pk)            ##############
#     return render(request,'courses/section_detail.html', {'section': section})##############


def step_detail(request, course_pk, section_pk):
    section = get_object_or_404(Section, course_id=course_pk, pk=section_pk)
    if Take.objects.filter(user=request.user, section=section):
        print('exist')
        return render(request, 'courses/reg_failed.html', {'section': section})
    else:
        section.capacity = section.capacity - 1
        Take.objects.create(user=request.user, section=section).save()

    return render(request, 'courses/step_detail.html', {'section': section})

