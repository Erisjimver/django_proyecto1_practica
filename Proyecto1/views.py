from django.http import HttpResponse
from django.template import Template,Context
import datetime

class Persona(object):

	def __init__(self,nombre,apellido):

		self.nombre=nombre
		self.apellido=apellido



def saludo2(request): #primera vista
	
	p1=Persona(" Alumno Israel", " Jimenez")
	temas_del_curso=["Plantillas","Modelos","Formularios","Vistas","Despliegue"]
	temas_del_curso1=[]
	ahora=datetime.datetime.now()
	doc_externo=open("C:/Users/Home/django/Proyecto1/Proyecto1/plantillas/miplantilla.html")
	plantilla=Template(doc_externo.read())
	doc_externo.close()
	contexto=Context({"nombre_persona":p1.nombre,"apellido_persona":p1.apellido, "momento_actual":ahora,"temas":temas_del_curso1})
	documento=plantilla.render(contexto)
	return HttpResponse(documento)



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