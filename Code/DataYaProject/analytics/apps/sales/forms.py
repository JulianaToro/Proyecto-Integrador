from django import forms
from .models import Sale

class SaleAnalysisForm(forms.Form):
    # Puedes agregar más campos de formulario según tus necesidades
    start_date = forms.DateField(label='Fecha de inicio')
    end_date = forms.DateField(label='Fecha de fin')
