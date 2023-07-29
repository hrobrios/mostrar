from django.contrib import admin
from appusos.models import Proyecto
# Register your models here.

class ProyectoAdmin(admin.ModelAdmin):
    list_display=["nombre", "fecha_inicio","fecha_termino", "responsable", "prioridad"]

admin.site.register(Proyecto)