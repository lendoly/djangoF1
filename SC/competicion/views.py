from django.shortcuts import render
from django.template import RequestContext, loader
from django.http import HttpResponse
from .models import Circuito, GranPremio
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
def index(request):
    template = loader.get_template('competicion/index.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))


def circuitos(request):
    cricuitos_list = Circuito.objects.all()
    template = loader.get_template('circuitos/index.html')
    context = RequestContext(request, {
        'cricuitos_list': cricuitos_list,
        })
    return HttpResponse(template.render(context))


def circuito_detail(request, circuito_id):
    try:
        circuito = Circuito.objects.get(id=circuito_id)
        context = {
            'circuito': circuito,
            'circuito_id': circuito_id,
            }
        return render(request, 'circuitos/detail.html', context)
    except ObjectDoesNotExist:
        return render(request, 'circuitos/detail.html',
                      {'circuito_id': circuito_id})


def grandes_premios(request):
    grandes_premios = GranPremio.objects.all()
    template = loader.get_template('gran_premio/index.html')
    context = RequestContext(request, {
        'grandes_premios': grandes_premios,
        })
    return HttpResponse(template.render(context))


def gran_premio(request, gran_premio_id):
    gran_premio = GranPremio.objects.get(id=gran_premio_id)
    print(gran_premio)
    context = {
        'gran_premio': gran_premio,
        'gran_premio_id': gran_premio_id,
        }
    return render(request, 'gran_premio/detail.html', context)
