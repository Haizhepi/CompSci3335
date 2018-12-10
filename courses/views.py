from django.shortcuts import get_object_or_404, render

from .models import Course, Step, Section


def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})


def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    section = get_object_or_404(Section, pk=pk)

    return render(request, 'courses/course_detail.html', {'course': course, 'section':section})


# def section_detail(request, pk):                            ##############
#     section = get_object_or_404(Section, pk=pk)            ##############
#     return render(request,'courses/section_detail.html', {'section': section})##############


def step_detail(request, course_pk, step_pk):
    step = get_object_or_404(Step, course_id=course_pk, pk=step_pk)
    return render(request, 'courses/step_detail.html', {'step': step})