from django import forms
import datetime
from .models import UserProfile
from django.contrib.auth import (
    authenticate,
    get_user_model
)
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User


class RegForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        )

    def save(self, commit=True):
        user = super(RegForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user


class EditProfileForm(UserChangeForm):

    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'password'
        )


class Profile_form(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = (
            'middle',
            'suffix',
            'address1',
            'address2',
            'city',
            'state',
            'zip',
            'phone',
            'grad_year',
            'birth_date',
            'accepted_to_GT_program',
            'english_learn',
            'student_grade',
        )

User = get_user_model()


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('user not exist')
            if not user.check_password(password):
                raise forms.ValidationError('Invalid password')
            if not user.is_active:
                raise forms.ValidationError('not active')

        return super(UserLoginForm, self).clean(*args, **kwargs)


def year_choices():
    return [(r,r) for r in range(1984, datetime.date.today().year+1)]


def current_year():
    return datetime.date.today().year


