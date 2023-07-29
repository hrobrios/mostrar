# importar desde django la utilidad forms
#django hace los input, imprime los html
from django import forms
from .models import Contacto

class ContactoForm(forms.ModelForm):
    
    class Meta:
        model = Contacto
        fields = "__all__"