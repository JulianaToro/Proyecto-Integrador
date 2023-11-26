from django.shortcuts import render
from django.views import View
from .forms import MarketingAnalysisForm
from dashboards.streamlit import run_streamlit_dashboard  # Importa la función para ejecutar el dashboard de Streamlit

class MarketingAnalysisView(View):
    template_name = 'marketing/analysis.html'  # Puedes personalizar la plantilla según tus necesidades

    def get(self, request, *args, **kwargs):
        form = MarketingAnalysisForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = MarketingAnalysisForm(request.POST)
        if form.is_valid():
            # Realiza el análisis automático aquí con los datos proporcionados por el formulario
            campaign_name = form.cleaned_data['campaign_name']

            # Llama a la función que ejecuta el dashboard de Streamlit
            run_streamlit_dashboard(campaign_name=campaign_name)

            # Puedes agregar más lógica aquí según sea necesario

        return render(request, self.template_name, {'form': form})
