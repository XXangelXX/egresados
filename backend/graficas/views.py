from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView
from chartjs.views.pie import HighChartPieView

@login_required(login_url='/')
def graficas(request):
    return render(request, 'graficas/grafica_base.html', {})


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

