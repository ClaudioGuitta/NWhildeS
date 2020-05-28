from django.forms import ModelForm
from django import forms

from .models import *


class DateForm(forms.DateInput):
    input_type = 'date'


class TarefaForm(ModelForm):
    class Meta:
        model = Tarefa
        fields = ['titulo','data_vencimento','descricao']
        widgets = {
            'data_vencimento': DateForm(),
        }
