from django.db import models



class Proyecto(models.Model):
	fecha_inicio = models.DateField()
	fecha_termino = models.DateField()	
	nombre = models.CharField(max_length=50)
	responsable = models.CharField(max_length=50)
	prioridad = models.PositiveIntegerField()

    

#este es el listado para tipo de consulta del formulario

opciones_consultas = [
	[0,"consulta"],
	[1, "reclamo"],
	[2, "sugerencia"],
	[3, "felicitaciones"]
]

class Contacto(models.Model):
	nombre = models.CharField(max_length=50)
	correo = models.EmailField()
	tipo_consulta = models.IntegerField(choices=opciones_consultas)
	mensaje = models.TextField()
	avisos = models.BooleanField()

    

