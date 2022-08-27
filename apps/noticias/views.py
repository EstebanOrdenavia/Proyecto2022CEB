from django.shortcuts import render

def noticias(request):
    return render(request, 'noticias/noticias.html')


def detalleNoticias(request):
    return render(request, 'noticias/detalleNoticias.html')