from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.application_list, name='application_home'),
    url(r'(?P<pk>\d+)/$', views.application_detail, name='application_detail'),
]