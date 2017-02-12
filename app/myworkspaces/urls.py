from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

import django.contrib.auth

urlpatterns = [
    # ex: /
    # url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^wp/$', views.workspaces, name='workspaces'),
    url(r'^wp/chat/$', views.chat, name='chat'),
    url(r'^wp/board/$', views.board, name='board'),
    url(r'^wp/docs/$', views.docs, name='docs'),
    url(r'^wp/calendar/$', views.calendar, name='calendar'),
    url(r'^node_api/$', views.node_api, name='node_api'),
    url(r'^wp/logout/$', auth_views.logout, {'template_name': 'logged_out.html'}, name='logout'),
    # url(r'^login/$', django.contrib.auth.views.login, {'template_name': 'admin/login.html'}, name='login'),
    # url(r'^logout/$', django.contrib.auth.views.logout, {'next_page': '/'}, name='logout'),
]