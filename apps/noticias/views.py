from django.shortcuts import render
from .models import Noticia
from django.views.generic.detail import DetailView


def noticias(request):

    noticias = Noticia.objects.all()

    return render(request, 'noticias/noticias.html', {'noticias': noticias})


def detalleNoticias(request, pk):

    notis = Noticia.objects.get(pk=pk)
    return render(request, 'noticias/detalleNoticias.html', {'notis': notis})

# class Detalle_Noticia_Clase(DetailView):
#     model = Noticia
#     template_name = 'noticias/detalleNoticias.html'