from django.shortcuts import render
from django.views import View
from .forms import CustomerAnalysisForm
from dashboards.streamlit import run_streamlit_dashboard  # Importa la función para ejecutar el dashboard de Streamlit

class CustomerAnalysisView(View):
    template_name = 'customers/analysis.html'  # Puedes personalizar la plantilla según tus necesidades

    def get(self, request, *args, **kwargs):
        form = CustomerAnalysisForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = CustomerAnalysisForm(request.POST)
        if form.is_valid():
            # Realiza el análisis automático aquí con los datos proporcionados por el formulario
            customer_id = form.cleaned_data['customer_id']

            # Llama a la función que ejecuta el dashboard de Streamlit
            run_streamlit_dashboard(customer_id=customer_id)

            # Puedes agregar más lógica aquí según sea necesario

        return render(request, self.template_name, {'form': form})
