from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path("lista-familiar/", lista_familiar),
    path('agregar-familia/<nombre>/<dni>/<nacimiento>', familiar),

]
