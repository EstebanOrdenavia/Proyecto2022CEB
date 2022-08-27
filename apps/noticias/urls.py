from django.urls import path
from . import views


app_name= 'noticias'
urlpatterns = [
    path("noticias/", views.noticias, name="noticias"),
    path("detalleNoticias", views.detalleNoticias, name="detalleNoticias"),
]