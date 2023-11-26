from django import forms
from .models import FinancialData

class FinancialAnalysisForm(forms.Form):
    # Puedes agregar más campos de formulario según tus necesidades
    year = forms.IntegerField(label='Año')
