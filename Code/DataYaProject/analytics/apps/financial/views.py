from django.shortcuts import render
from django.views import View
from .forms import FinancialAnalysisForm
from dashboards.streamlit import run_streamlit_dashboard  # Importa la función para ejecutar el dashboard de Streamlit

class FinancialAnalysisView(View):
    template_name = 'financial/analysis.html'  # Puedes personalizar la plantilla según tus necesidades

    def get(self, request, *args, **kwargs):
        form = FinancialAnalysisForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = FinancialAnalysisForm(request.POST)
        if form.is_valid():
            # Realiza el análisis automático aquí con los datos proporcionados por el formulario
            year = form.cleaned_data['year']

            # Llama a la función que ejecuta el dashboard de Streamlit
            run_streamlit_dashboard(year=year)

            # Puedes agregar más lógica aquí según sea necesario

        return render(request, self.template_name, {'form': form})
