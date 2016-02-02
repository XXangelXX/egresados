from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from . import views


urlpatterns=patterns('formulario.views',
    #  /egresado/
    url(r'registro/', 'registro', name='registro'),
    #url(r'^/empresa/', 'datos_empresa', name='datos_empresa'),
    #url(r'^/datoslaborales/', 'datos_laborales', name='datos_laborales'),
    #url(r'^gracias/', 'encuesta_completa', name='encuesta_completa'),
    url(r'actualizar/', 'actualizar', name='actualizar'),
    url(r'change_password/', 'change_password', name='change_password'),
    url(r'perfil/', 'actualizar_perfil', name='actualizar_peril'),
    url(r'datoslaborales/', 'actualizar_datoslab', name='actualizar_datoslab'),
    url(r'empresa/', 'actualizar_empresa', name='actualizar_empresa'),
    url(r'occ/', 'ligaocc', name='ligaocc'),


)
