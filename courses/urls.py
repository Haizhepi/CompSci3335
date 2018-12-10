from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.course_list, name='list'),
    url(r'(?P<course_pk>\d+)/(?P<section_pk>\d+)/$', views.step_detail,
       name='section'),
    # url(r'(?P<pk>\d+)/$', views.section_detail,
    #     name='section'),
    url(r'(?P<pk>\d+)/$', views.course_detail, name='detail'),
]