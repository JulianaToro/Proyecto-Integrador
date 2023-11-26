from django.shortcuts import render
from django.views import View
from .forms import SaleAnalysisForm
from dashboards.streamlit import run_streamlit_dashboard  # Importa la función para ejecutar el dashboard de Streamlit

class SaleAnalysisView(View):
    template_name = 'sales/analysis.html'  # Puedes personalizar la plantilla según tus necesidades

    def get(self, request, *args, **kwargs):
        form = SaleAnalysisForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = SaleAnalysisForm(request.POST)
        if form.is_valid():
            # Realiza el análisis automático aquí con los datos proporcionados por el formulario
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']

            # Llama a la función que ejecuta el dashboard de Streamlit
            run_streamlit_dashboard(start_date, end_date)

            # Puedes agregar más lógica aquí según sea necesario

        return render(request, self.template_name, {'form': form})
