from django.http import HttpResponse
from django.template import Template,Context
from django.template import loader
from django.template.loader import get_template# sirve para evitar usar loader al llamar a un template
from django.shortcuts import render
import datetime

class Persona(object):

	def __init__(self,nombre,apellido):

		self.nombre=nombre
		self.apellido=apellido

def cursoC(request):
	fecha_actual=datetime.datetime.now()
	return render(request,"cursoC.html",{"dame_fecha":fecha_actual})

def cursoCSS(request):
	fecha_actual=datetime.datetime.now()
	return render(request,"cursoCSS.html",{"dame_fecha":fecha_actual})


def saludo2(request): #primera vista
	
	p1=Persona(" Alumno Israel", " Jimenez")
	temas_del_curso=["Plantillas","Modelos","Formularios","Vistas","Despliegue"]
	temas_del_curso1=[]
	ahora=datetime.datetime.now()
	#doc_externo=open("C:/Users/Home/django/Proyecto1/Proyecto1/plantillas/miplantilla.html")
	#plantilla=Template(doc_externo.read())
	#doc_externo.close()
	doc_externo=get_template('miplantilla.html')

	#contexto=Context({"nombre_persona":p1.nombre,"apellido_persona":p1.apellido, "momento_actual":ahora,"temas":temas_del_curso1})
	contexto={"nombre_persona":p1.nombre,"apellido_persona":p1.apellido, "momento_actual":ahora,"temas":temas_del_curso}
	#documento=plantilla.render(contexto)
	documento=doc_externo.render(contexto)
	#return HttpResponse(documento)
	return render(request,"miplantilla.html",contexto)
	#return HttpResponse(request,'miplantilla','{"nombre_persona":p1.nombre,"apellido_persona":p1.apellido, "momento_actual":ahora,"temas":temas_del_curso1}')



##

def saludo(request): #primera vista
	nombre="Israel"
	apellido="Jimenez"
	ahora=datetime.datetime.now()
	doc_externo=open("C:/Users/Home/django/Proyecto1/Proyecto1/plantillas/miplantilla.html")
	plantilla=Template(doc_externo.read())
	doc_externo.close()
	contexto=Context({"nombre_persona":nombre,"apellido_persona":apellido, "momento_actual":ahora})
	documento=plantilla.render(contexto)
	return HttpResponse(documento)

def despedida(request): #segunda vista
	return HttpResponse("Adios mundo")

def dame_fecha(request): #tercer vista

	fecha_actual=datetime.datetime.now()

	documento="""<html>

	<body>
	<h1>
	Fecha y hora actuales %s
	</h1>
	</body>

	</html>""" % fecha_actual

	return HttpResponse(documento)

def calcularEdad(request, anio):#cuarta vista

	edadActual=26
	periodo=anio-2019
	edadFutura=edadActual+periodo

	documento="<html><body><h1>En el año %s tendras %s años "%(anio,edadFutura)

	return HttpResponse(documento)

def calcularEdad1(request,edad, anio):#cuarta vista

	periodo=anio-2019
	edadFutura=edad+periodo

	documento="<html><body><h1>En el año %s tendras %s años "%(anio,edadFutura)

	return HttpResponse(documento)