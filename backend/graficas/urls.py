from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from . import views


urlpatterns=patterns('graficas.views',
    
    url(r'^$', 'graficas', name='graficas'),
    url(r'^line_chart/$', views.line_chart,
        name='line_chart'),
    url(r'^line_chart/json/$', views.line_chart_json,
        name='line_chart_json'),
    url(r'^circular_titulado/$', views.circular_titulado,
        name='circular_titulado'),
    url(r'^circular_titulado/json/$', views.circular_titulado_json,
        name='circular_titulado_json'),


)