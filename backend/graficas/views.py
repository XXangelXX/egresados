# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from django.views.generic import TemplateView
from django.db.models import Q

from .datos_generales import lista_anios, lista_meses, lista_carreras, lista_filtros

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
        total_egresados = PerfilEgresado.objects.all().count()
        cxt= {'lista_anios': lista_anios,'data_labels':lista_anios, 'data_general': datae_anio,
        'grafica_titulo':"GRAFICA GENERAL", 'grafica_anio': 'Desde 1985 a 2015', 'grafica_filtros': 'Sin Filtros',
        'totales' : total_egresados}
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
            q = q.filter(Q(ocupacion=1) | Q(ocupacion=3))
            return q

def graficacion(q,c,a,t):
    data_cxt = []
    cxt = {}
    if c == "TODOS" and a == "TODOS" and t == "TODOS":
        data_cxt = filtro_carreras(q)
        total_egresados = q.all().count()
        cxt= {'lista_anios': lista_anios,'data_labels':lista_carreras, 'data_general': data_cxt,
        'grafica_titulo':"Grafica de Egresados de Todas las Carreras", 'grafica_anio': 'Desde 1985 a 2015', 'grafica_filtros': 'Sin Filtros',
        'totales' : total_egresados}
        return cxt
    elif c!="TODOS" and a == "TODOS" and t == "TODOS":
        data_cxt = filtro_anios(q)
        total_egresados = q.all().count()
        titulo_carrera = "Grafica de Egresados de la Carrera: " + lista_carreras[int(c)-1]
        cxt= {'lista_anios': lista_anios,'data_labels':lista_anios, 'data_general': data_cxt,
        'grafica_titulo': titulo_carrera, 'grafica_anio': 'Desde 1985 a 2015', 'grafica_filtros': 'Sin Filtros',
        'totales' : total_egresados}
        return cxt
    elif c!="TODOS" and a!="TODOS" and t=="TODOS":
        data_cxt = filtro_meses(q)
        total_egresados = q.all().count()
        titulo_carrera = "Grafica de Egresados de la Carrera: " + lista_carreras[int(c)-1]
        anio_titulo = "En el año: " + str(a)
        cxt= {'lista_anios': lista_anios,'data_labels':lista_meses, 'data_general': data_cxt,
        'grafica_titulo': titulo_carrera, 'grafica_anio': anio_titulo, 'grafica_filtros': 'Sin Filtros',
        'totales' : total_egresados}
        return cxt
    elif c!="TODOS" and a!="TODOS" and t!="TODOS":
        data_cxt = filtro_carreras(q)
        total_egresados = q.all().count()
        titulo_carrera = "Grafica de Egresados de la Carrera: " + lista_carreras[int(c)-1]
        anio_titulo = "En el año: " + str(a)
        filtro_titulo = "Filtro por: " + lista_filtros.get(int(t))
        cxt= {'lista_anios': lista_anios,'data_labels':lista_meses, 'data_general': data_cxt,
        'grafica_titulo': titulo_carrera, 'grafica_anio': anio_titulo, 'grafica_filtros': filtro_titulo,
        'totales' : total_egresados}
        return cxt
    elif c!="TODOS" and a=="TODOS" and t!="TODOS":
        data_cxt = filtro_anios(q)
        total_egresados = q.all().count()
        titulo_carrera = "Grafica de Egresados de la Carrera: " + lista_carreras[int(c)-1]
        anio_titulo = "Todos los Años: desde 1985 a 2015"
        filtro_titulo = "Filtro por: " + lista_filtros.get(int(t))
        cxt= {'lista_anios': lista_anios,'data_labels':lista_anios, 'data_general': data_cxt,
        'grafica_titulo': titulo_carrera, 'grafica_anio': anio_titulo, 'grafica_filtros': filtro_titulo,
        'totales' : total_egresados}
        return cxt
    elif c=="TODOS" and a=="TODOS" and t!="TODOS":
        data_cxt = filtro_carreras(q)
        total_egresados = q.all().count()
        titulo_carrera = "Grafica de Egresados de todas las Carreras "
        anio_titulo = "Todos los Años: desde 1985 a 2015"
        filtro_titulo = "Filtro por: " + lista_filtros.get(int(t)) 
        cxt= {'lista_anios': lista_anios,'data_labels':lista_carreras, 'data_general': data_cxt,
        'grafica_titulo': titulo_carrera, 'grafica_anio': anio_titulo, 'grafica_filtros': filtro_titulo,
        'totales' : total_egresados}
        return cxt
    elif c=="TODOS" and a!="TODOS" and t=="TODOS":
        data_cxt = filtro_carreras_anio(q,a)
        titulo_carrera = "Grafica de Egresados de todas las Carreras "
        anio_titulo = "En el año: " + str(a)
        filtro_titulo = "Filtro por: Sin Filtro "  
        cxt= {'lista_anios': lista_anios,'data_labels':lista_carreras, 'data_general': data_cxt,
        'grafica_titulo': titulo_carrera, 'grafica_anio': anio_titulo, 'grafica_filtros': filtro_titulo}
        return cxt

    

def filtro_meses(q):
    data_cxt = []
    for mes in range(1,13):
        data_cxt.append(q.filter(mes_anio_egreso__month=mes).count())
    return data_cxt

def filtro_anios(q):
    data_cxt = []
    for anio in range (1985,2016):
        data_cxt.append(q.filter(mes_anio_egreso__year=anio).count())
    return data_cxt

def filtro_carreras(q):
    data_cxt = []
    for carrera_f in range (1,12):
        data_cxt.append(q.filter(carrera=carrera_f).count())
    return data_cxt

def filtro_carreras_anio(q,a):
    data_cxt = []
    for carrera_f in range (1,12):
        data_cxt.append(q.filter(carrera=carrera_f).filter(mes_anio_egreso__year=int(a)).count())
    return data_cxt



