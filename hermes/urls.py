from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
from . import views

urlpatterns = patterns('',
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^$', views.home, name='home'),

    url(r'^collection/(?P<collection_id>[0-9]+)/$', views.collection, name='collection'),
    url(r'^collection/(?P<collection_id>[0-9]+)/ressource/add$', views.ressource_add, name='ressource_add'),

)
