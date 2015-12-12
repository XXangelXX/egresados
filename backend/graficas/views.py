# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from django.views.generic import TemplateView

from .datos_generales import lista_anios, lista_meses, lista_carreras

from perfil.models import PerfilEgresado


def graficas(request):
    """Grafica General por Años"""
    cxt = {}
    if request.method=='POST':

        if request.POST.get('carrerag_f','')== "GENERAL":
            return redirect('/graficas/') 
        else:
            c = request.POST.get('carrerag_f','')
            a = request.POST.get('anio_f','')
            t = request.POST.get('titulado_f','')

            egresados = PerfilEgresado.objects.all()
            qc = carreras(request, egresados)
            qa = anios(request, qc)
            qt = titulado(request, qa)
            cxt = graficacion(qt, c, a, t)

            return render(request, 'graficas/grafica_base.html', cxt)   


    else:
        datae_anio=[]
        for anio in range(1985,2016):
            datae_anio.append(PerfilEgresado.objects.filter(mes_anio_egreso__year=anio).count())
        cxt= {'lista_anios': lista_anios,'data_labels':lista_anios, 'data_general': datae_anio}
        return render(request, 'graficas/grafica_base.html', cxt)   


def carreras (request, q):
    if request.POST.get('carrerag_f','') == "TODOS":
        return q
    else:
        q = q.filter(carrera=int(request.POST.get('carrerag_f','')))
        return q

def anios (request, q ):
    if request.POST.get('anio_f','') == "TODOS":
        return q
    else: 
        q = q.filter(mes_anio_egreso__year=int(request.POST.get('anio_f','')))
        return q

def titulado(request, q):
    if request.POST.get('titulado_f','') =="TODOS": 
        return q
    else:
        if request.POST.get('titulado_f','') =="0":
            q = q.filter(titulado=0)
            return q
        elif request.POST.get('titulado_f','') =="1":
            q = q.filter(titulado=1)
            return q
        elif request.POST.get('titulado_f','') =="2":
            q = q.filter(ocupacion=1)
            return q

def graficacion(q,c,a,t):
    data_cxt = []
    cxt = {}
    if c == "TODOS" and a == "TODOS" and t == "TODOS":
        for carrera_f in range (1,12):
            data_cxt.append(q.filter(carrera=carrera_f).count())
        cxt= {'lista_anios': lista_anios,'data_labels':lista_carreras, 'data_general': data_cxt}
        return cxt
    elif c!="TODOS" and a == "TODOS" and t == "TODOS":
        for anio in range (1985,2016):
            data_cxt.append(q.filter(mes_anio_egreso__year=anio).count())
        cxt= {'lista_anios': lista_anios,'data_labels':lista_anios, 'data_general': data_cxt}
        return cxt
    elif c!="TODOS" and a!="TODOS" and t=="TODOS":
        for mes in range(1,13):
            data_cxt.append(q.filter(mes_anio_egreso__month=mes).count())
        cxt= {'lista_anios': lista_anios,'data_labels':lista_meses, 'data_general': data_cxt}
        return cxt
    elif c!="TODOS" and a!="TODOS" and t!="TODOS":
        for mes in range(1,13):
            data_cxt.append(q.filter(mes_anio_egreso__month=mes).count())
        cxt= {'lista_anios': lista_anios,'data_labels':lista_meses, 'data_general': data_cxt}
        return cxt 
    elif c!="TODOS" and a=="TODOS" and t!="TODOS":
        for anio in range (1985,2016):
            data_cxt.append(q.filter(mes_anio_egreso__year=anio).count())
        cxt= {'lista_anios': lista_anios,'data_labels':lista_anios, 'data_general': data_cxt}
        return cxt 
    elif c=="TODOS" and a=="TODOS" and t!="TODOS":
        for carrera_f in range (1,12):
            data_cxt.append(q.filter(carrera=carrera_f).count())
        cxt= {'lista_anios': lista_anios,'data_labels':lista_carreras, 'data_general': data_cxt}
        return cxt
        