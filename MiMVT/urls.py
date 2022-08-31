from django.urls import path

from MiMVT.views import datos_madre, datos_padre, datos_tio

urlpatterns = [
    path('padre/', datos_padre),
    path('madre/', datos_madre),
    path('tio/',datos_tio)
]