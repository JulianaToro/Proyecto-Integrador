from django import forms
from .models import MarketingCampaign

class MarketingAnalysisForm(forms.Form):
    # Puedes agregar más campos de formulario según tus necesidades
    campaign_name = forms.CharField(label='Nombre de la campaña')
