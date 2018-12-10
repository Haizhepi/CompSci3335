from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
    update_session_auth_hash,
)
from .models import UserProfile
from django.contrib.auth.decorators import login_required
from .forms import (
    RegForm, UserLoginForm, EditProfileForm,
)
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm


def login_view(request):
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect('/')
    context = {
        'form': form
    }

    return render(request, 'accounts/login.html', context)


def register_view(request):
    if request.method == 'POST':
        form = RegForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = RegForm()

    context = {
        'form': form
    }

    return render(request, 'accounts/signup.html', context)


def logout_view(request):
    logout(request)
    return redirect('/')


@login_required
def profile_view(request):
    if UserProfile.objects.filter(user=request.user):
        profile = UserProfile.objects.get(user=request.user)
        args = {'user': request.user, 'profile': profile}

        return render(request, 'accounts/profile.html', args)
    else:
        return render(request, "courses/profile_incomplete.html", {'message': 'You must finish your profile first'})


@login_required
def edit_profile_view(request):
    if request.method == 'POST':
        form1 = None
        form2 = None
        if UserProfile.objects.filter(user=request.user):
            form1 = EditProfileForm(request.POST, instance=request.user)
            form2 = forms.Profile_form(request.POST, instance=UserProfile.objects.get(user=request.user))
        else:
            form1 = EditProfileForm(request.POST, instance=request.user)
            form2 = forms.Profile_form(request.POST)
        if form1.is_valid() and form2.is_valid():
            form1.save()
            obj = form2.save(commit=False)
            obj.user = request.user
            obj.save()
            return redirect('/accounts/profile')
    else:
        if UserProfile.objects.filter(user=request.user):
            form1 = EditProfileForm(instance=request.user)
            form2 = forms.Profile_form(instance=UserProfile.objects.get(user=request.user))
            args = {'form1': form1, 'form2': form2}
            return render(request, 'accounts/edit_profile.html', args)
        else:
            form1 = EditProfileForm()
            form2 = forms.Profile_form()
            args = {'form1': form1, 'form2': form2}
            return render(request, 'accounts/edit_profile.html', args)


@login_required
def change_pw_view(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/accounts/profile')
        else:
            return redirect('/accounts/change_password')
    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}

        return render(request, 'accounts/change_password.html', args)




