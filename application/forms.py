from django import forms
from .models import School, Parent


class SchoolForm(forms.ModelForm):

    class Meta:
        model = School
        fields = (
            'type',
            'school_name',
            'grade'
        )


class ParentForm(forms.ModelForm):

    class Meta:
        model = Parent
        fields = (
            'name',
            'address',
            'email',
            'cell_phone',
            'home_phone',
            'work_phone',
        )