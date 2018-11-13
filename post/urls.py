from django.conf.urls import url, include

from blog import settings
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import logout

from django.contrib.auth.views import logout
from blog import settings

from post.views import *

from django.conf.urls import url
from django.conf import settings
from django.contrib.auth.views import logout

urlpatterns = [
    url(r'^$', index),
    url(r'^(?P<pk>\d+)/$', post_detail, name='post_detail'),
    url(r'^delete/(?P<pk>\d+)/$', delete_post, name='delete_post'),
    url(r'^edit/(?P<pk>\d+)/$', edit_post, name='edit_post'),
    url(r'create-post/$', create_post),

    url(r'pub/(?P<pk>\d+)/$', publish),

    #url(r'^logout/$', logout, {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
    url(r'^logout/$', logout, {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),


    url(r'^tinymce/', include('tinymce.urls')),
    ]
