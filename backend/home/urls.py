from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from . import views


urlpatterns=patterns('home.views',
    url(r'^$', 'index_view', name='index'),
    url(r'^olvidec/', 'olvidec', name='info'),
    url(r'^home/', 'home', name='home'),
    url(r'^carrera/', 'carrera', name='carrera'),
    url(r'^logout/', 'log_out', name='log_out'),
)