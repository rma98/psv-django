from django import forms
from .models import Medico

class formMedico(forms.ModelForm):
    class Meta:
        model = Medico
        fields= ('nome','CRM','especializacao','turno','email','senha')
