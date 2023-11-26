from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import AnalysisReport
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

class UploadExcelView(View):
    def post(self, request):
        excel_file = request.FILES['excel_file']
        data = pd.read_excel(excel_file)

        # Preparar los datos para el aprendizaje automático
        y = data['ventas']
        X = data.drop('ventas', axis=1)
        X_train, X_valid, y_train, y_valid = train_test_split(X, y, train_size=0.8, test_size=0.2)

        # Definir el modelo
        model = RandomForestRegressor(n_estimators=100, random_state=0)

        # Ajustar el modelo
        model.fit(X_train, y_train)

        # Obtener predicciones
        preds = model.predict(X_valid)

        # Calcular el error medio absoluto (MAE)
        mae = mean_absolute_error(y_valid, preds)

        # Crear el informe
        report = f'Error Medio Absoluto del modelo: {mae}'

        response = HttpResponse(report, content_type='text/plain')
        response['Content-Disposition'] = 'attachment; filename="report.txt"'

        return response

def database_list(request):
    databases = AnalysisReport.objects.all()
    return render(request, 'analytics/database_list.html', {'databases': databases})

