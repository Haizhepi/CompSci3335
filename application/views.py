from .models import Application
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from .models import Parent, School
from django.core.exceptions import ObjectDoesNotExist
from accounts.forms import (
    RegForm, UserLoginForm, EditProfileForm,forms, Profile_form,
)

from .forms import SchoolForm, ParentForm
from accounts.models import UserProfile


# Create your views here.


def application_list(request):
    # applications = get_object_or_404(Application, user=request.user)

    applications = Application.objects.all()
    listapp = []
    for application in applications:
        if application.user == request.user:
            listapp.append(application)

    return render(request, 'application/application_home.html', {'applications': listapp})


@login_required
def application_detail(request, pk):
    application = get_object_or_404(Application, pk=pk)
    return render(request, 'application/application_detail.html', {'application': application})


@login_required
def application_profile(request):
    if request.method == 'POST':
        form1 = EditProfileForm(request.POST, instance=request.user)
        form2 = None
        temp = None
        try:
            temp = UserProfile.objects.get(user=request.user)
            form2 = Profile_form(request.POST, instance=temp)
        except UserProfile.DoesNotExist:
            form2 = Profile_form(request.POST)
        if form1.is_valid() and form2.is_valid():
            form1.save()
            obj = form2.save(commit=False)
            obj.user = request.user
            obj.save()
            return redirect('application:application_home')
        else:
            return redirect('application:application_profile')
    else:
        form1 = EditProfileForm(instance=request.user)
        try:
            temp = UserProfile.objects.get(user=request.user)
            form2 = Profile_form(request.POST, instance=temp)
        except UserProfile.DoesNotExist:
            form2 = Profile_form()
        args = {'form1': form1, 'form2': form2}

        return render(request, 'accounts/edit_profile.html', args)


@login_required
def application_school(request):
    if request.method == 'POST':
        form = SchoolForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            return redirect('application:application_home')
    else:
        form = SchoolForm(instance=request.user)
        args = {'form': form}
        return render(request, 'application/school.html', args)


@login_required
def application_parent(request):
    if request.method == 'POST':
        form = ParentForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            return redirect('application:application_home')
    else:
        form = ParentForm(instance=request.user)
        args = {'form': form}
        return render(request, 'application/parent.html', args)


def application_start(request):
    valid = True
    args = {}
    user_profile = None
    try:
         user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        valid = False
        args['profile'] = 'Incomplete profile'

    try:
        parent = []
        parent.append(Parent.objects.filter(user=request.user))
    except ObjectDoesNotExist:
        valid = False
        args['parent'] ='No parent is related to your account'

    try:
        school = []
        school.append(School.objects.filter(user=request.user))
    except ObjectDoesNotExist:
        valid = False
        args['school'] = 'No school is related to your account'

    if valid:
        app = Application.objects.create(user=request.user, user_profile=UserProfile.objects.get(user=request.user))
        app.application_status = 'P'
        app.save()
        return render(request, 'application/success.html', args)
    else:
        return render(request, 'application/Failed.html', args)







