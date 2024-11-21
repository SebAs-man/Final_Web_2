from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Card


# Create your views here.
def index(request):
    lista_cartas = Card.objects.all()
    template = loader.get_template('index.html')

    context = {"Cartas": lista_cartas}
    return HttpResponse(template.render(context, request))


def vista_detalle(request, name):
    detalle = Card.objects.get(name=name)
    template = loader.get_template("detail.html")

    context = {"carta": detalle}
    return HttpResponse(template.render(context, request))
