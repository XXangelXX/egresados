from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView


urlpatterns=patterns('home.views',
    url(r'^$', 'index_view', name='index'),
    url(r'^info/', 'info', name='info'),

)