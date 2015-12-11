# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView
from chartjs.views.pie import HighChartPieView
from .datos_generales import lista_anios, lista_meses

from perfil.models import PerfilEgresado


def graficas(request):
    """Grafica General por Años"""
    cxt = {}
    if request.method=='POST':
        if request.POST.get('anio_f',''):
            f_anio = int(request.POST.get('anio_f',''))
            q = PerfilEgresado.objects.filter(mes_anio_egreso__year=f_anio)
            datae_meses=[]
            for mes in range(1,13):
                datae_meses.append(q.filter(mes_anio_egreso__month=mes).count())
            cxt= {'lista_anios': lista_anios, 'data_general': datae_meses,
                'data_labels':lista_meses}
            return render(request, 'graficas/grafica_base.html', cxt)
    else:
        datae_anio=[]
        for anio in range(1985,2016):
            datae_anio.append(PerfilEgresado.objects.filter(mes_anio_egreso__year=anio).count())
        cxt= {'lista_anios': lista_anios,'data_labels':lista_anios, 'data_general': datae_anio}
        return render(request, 'graficas/grafica_base.html', cxt)
        
    return render(request, 'graficas/grafica_base.html', cxt)




class LineChartJSONView(BaseLineChartView):
    def get_labels(self):
        """Return 7 labels."""
        return ["January", "February", "March", "April", "May", "June", "July"]

    def get_data(self):
        """Return 3 dataset to plot."""

        return [[75, 44, 92, 11, 44, 95, 35],
                [41, 92, 18, 3, 73, 87, 92],
                [87, 21, 94, 3, 90, 13, 65]]


line_chart = TemplateView.as_view(template_name='graficas/graficalineal.html')
line_chart_json = LineChartJSONView.as_view()

class CircularTituladoJSONView(HighChartPieView):
    def get_labels(self):
        """Return 7 labels."""
        return ["January", "February", "March", "April", "May", "June", "July"]

    def get_data(self):
        """Return 3 dataset to plot."""

        return [[75, 44, 92, 11, 44, 95, 35],
                [41, 92, 18, 3, 73, 87, 92],
                [87, 21, 94, 3, 90, 13, 65]]


circular_titulado = TemplateView.as_view(template_name='graficas/grafica_circular.html')
circular_titulado_json = CircularTituladoJSONView.as_view()

