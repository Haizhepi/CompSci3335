from .models import Application
from django.shortcuts import get_object_or_404, render

# Create your views here.


def application_list(request):
    applications = Application.objects.all()
    return render(request, 'application/application_home.html', {'applications': applications})


def application_detail(request, pk):
    application = get_object_or_404(Application, pk=pk)
    return render(request, 'application/application_detail.html', {'application': application})
