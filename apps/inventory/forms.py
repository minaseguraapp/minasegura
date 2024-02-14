from django import forms
from django.forms import ModelForm

from .models import Maintenance


class MaintenanceForm(ModelForm):
    class Meta:
        model = Maintenance
        fields = ['equipment', 'description', 'priority', 'work_time', 'work_started_time', 'work_end_time']
        labels = {
            'equipment': 'Equipo',
            'description': 'Descripción',
            'priority': 'Prioridad',
            'work_time': 'Tiempo de trabajo',
            'work_started_time': 'Hora de inicio de trabajo',
            'work_end_time': 'Hora de fin de trabajo',
        }
        widgets = {
            'equipment': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'priority': forms.Select(attrs={'class': 'form-control'}),
            'work_time': forms.NumberInput(attrs={'class': 'form-control'}),
            'work_started_time': forms.DateTimeInput(
                attrs={'class': 'form-control', 'type': 'datetime-local', }),
            'work_end_time': forms.DateTimeInput(
                attrs={'class': 'form-control', 'type': 'datetime-local', }),
        }
        error_messages = {
            'equipment': {
                'required': 'Este campo es requerido',
            },
            'description': {
                'required': 'Este campo es requerido',
            },
            'priority': {
                'required': 'Este campo es requerido',
            },
            'work_time': {
                'required': 'Este campo es requerido',
            },
        
        }
