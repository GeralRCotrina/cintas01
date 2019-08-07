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

class AljForm(forms.ModelForm): 

	class Meta:
		model = Alojadores

		fields = ['nombre','ubicacion_cot','tamano']	

		labels = {
			'nombre':'Nombre',
			'ubicacion_cot':'Se encuentra en',
			'tamano':'Tamaño',
		}

		widgets={	
			    'nombre':forms.TextInput(attrs={'class':'form-control'}),
			    'ubicacion_cot':forms.TextInput(attrs={'class':'form-control','type':'text'}),
			    'tamano':forms.TextInput(attrs={'class':'form-control','type':'number'}),
		    }
  


class ProyForm(forms.ModelForm): 

	class Meta:
		model = Proyectos

		fields = ['nombre','cliente','alp','descripcion']	

		labels = {
			'nombre':'Proyecto',
			'cliente':'Cliente',
			'alp':'ALP',
			'descripcion':'Descripción',
		}

		widgets={	
			    'nombre':forms.TextInput(attrs={'class':'form-control'}),
			    'cliente':forms.TextInput(attrs={'class':'form-control','type':'text'}),
			    'alp':forms.TextInput(attrs={'class':'form-control','type':'number','col':'2'}),
			    'descripcion':forms.TextInput(attrs={'class':'form-control'}),
		    }
  




