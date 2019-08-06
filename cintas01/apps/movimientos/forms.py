from django import forms
from apps.movimientos.models import *


class MovimientoForm(forms.ModelForm):

	class Meta:
		model = Movimiento

		fields = ['id_asuth','fecha','hora','razon']	

		labels = {
			'id_asuth':'Usuario',
			'fecha':'Fecha',
			'hora':'Hora',
			'razon':'Descripción',
		}

		widgets={	
			    'id_asuth':forms.Select(attrs={'class':'form-control'}),
			    'fecha':forms.DateInput(attrs={'class':'form-control','type':'date'}),
			    'hora':forms.TimeInput(attrs={'class':'form-control','type':'date'}),
			    'razon':forms.TextInput(attrs={'class':'form-control'}),
		    }

