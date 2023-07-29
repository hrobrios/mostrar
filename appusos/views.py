from django.shortcuts import render
from .models import Contacto
from .forms import ContactoForm #se importan los formulario desde forms

# Create your views here.

def contacto(request):
	data = {
		"form": ContactoForm() #es una instancia de un formulario vacio
	}
	return render(request, "contacto.html", data)

