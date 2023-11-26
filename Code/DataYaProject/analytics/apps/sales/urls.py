from django.urls import path
from .views import SaleAnalysisView

app_name = 'sales'
urlpatterns = [
    path('analyze/', SaleAnalysisView.as_view(), name='analyze_sales'),
]
