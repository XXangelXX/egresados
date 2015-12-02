from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from . import views


urlpatterns=patterns('home.views',
    url(r'^$', 'index_view', name='index'),
    url(r'^info/', 'info', name='info'),
    url(r'^graficas/', 'graficas', name='graficas'),
    url(r'^home/', 'home', name='home'),
    url(r'^carrera/', 'carrera', name='carrera'),
    url(r'^logout/', 'log_out', name='log_out'),
    url(r'^graficas/line_chart/$', views.line_chart,
        name='line_chart'),
    url(r'^graficas/line_chart/json/$', views.line_chart_json,
        name='line_chart_json'),
    url(r'^graficas/circular_titulado/$', views.circular_titulado,
        name='circular_titulado'),
    url(r'^graficas/circular_titulado/json/$', views.circular_titulado_json,
        name='circular_titulado_json'),


)