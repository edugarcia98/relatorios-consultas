from django.shortcuts import render
from django.http import HttpResponse
from .models import Consulta

import datetime

# Create your views here.
def index(request):
    consultas = Consulta.objects.order_by('numero_guia')

    filter_medico = request.GET.get('filter_medico')
    if filter_medico != '':
        consultas = consultas.filter(medico__nome_medico__iexact=filter_medico)

    filter_periodo_inicial = request.GET.get('filter_periodo_inicial')
    if filter_periodo_inicial != '':
        filter_periodo_inicial = datetime.datetime.strptime(filter_periodo_inicial, '%Y-%m-%d')
        consultas = consultas.filter(data_consulta__gte=filter_periodo_inicial)

    filter_periodo_final = request.GET.get('filter_periodo_final')
    if filter_periodo_final != '':
        filter_periodo_final = datetime.datetime.strptime(filter_periodo_final, '%Y-%m-%d')
        consultas = consultas.filter(data_consulta__lte=filter_periodo_final)

    context = {'consultas': consultas}
    return render(request, 'app/index.html', context)