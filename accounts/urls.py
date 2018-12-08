from django.conf.urls import url

from .views import register_view, logout_view, login_view, profile_view, edit_profile_view, change_pw_view
from django.contrib.auth.views import (
    password_reset, password_reset_done, password_reset_confirm, password_reset_complete
)
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^login/$', login_view, name='login'),
    url(r'^register/$', register_view, name='signup'),
    url(r'^logout/$', logout_view, name='logout'),
    url(r'^profile/$', profile_view, name='profile'),
    url(r'^edit/$', edit_profile_view, name='edit_profile'),
    url(r'^change_password/$', change_pw_view, name='change_pw'),
    url(r'^reset-password/$', password_reset, name='password_reset'),
    url(r'^reset-password/done/$', password_reset_done, name='password_reset_done'),
    url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm,
        name='password_reset_confirm'),
    url(r'^reset-password/complete/$', password_reset_complete, name='password_reset_complete'),

]