from django.urls import path
from .views import FinancialAnalysisView

app_name = 'financial'

urlpatterns = [
    path('analyze/', FinancialAnalysisView.as_view(), name='analyze_financial'),
]
