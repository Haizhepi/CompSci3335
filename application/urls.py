from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.application_list, name='application_home'),
    url(r'^school/$', views.application_school, name='application_school'),
    url(r'^parent/$', views.application_parent, name='application_parent'),
    url(r'(?P<pk>\d+)/$', views.application_detail, name='application_detail'),
    url(r'^finish_profile/$', views.application_profile, name='application_profile'),
    url(r'^start_application/$', views.application_start, name='application_start'),

]