from django import forms
from .models import Customer

class CustomerAnalysisForm(forms.Form):
    # Puedes agregar más campos de formulario según tus necesidades
    customer_id = forms.IntegerField(label='ID del Cliente')
