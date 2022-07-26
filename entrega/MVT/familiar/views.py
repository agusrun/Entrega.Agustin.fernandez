from django.shortcuts import render
from .models import familia
from django.http import HttpResponse

def familiar(self, nombre, dni, nacimiento):
    familiares = familia(nombre =  nombre , dni = dni, nacimiento = nacimiento)
    familiares.save()

    return HttpResponse(f'''
    <p> El familiar <strong>{familiares.nombre}</strong> de Dni <strong>{familiares.dni} </strong>, se ha agregado correctamente</p>
    ''')

def lista_familiar(self):
    lista = familia.objects.all()
    return render(self, 'inicio.html',{'lista_familiares': lista})
