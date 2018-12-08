from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from . import forms


def home(request):
    return render(request, 'home.html')


def suggestion_view(request):
    form = forms.SuggestionForm()
    if request.method == 'POST':
        form = forms.SuggestionForm(request.POST)
        if form.is_valid():
            print('good form')
    return render(request, 'suggestion_form.html', {'form': form})