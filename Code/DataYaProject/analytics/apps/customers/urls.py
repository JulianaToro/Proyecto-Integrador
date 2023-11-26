from django.urls import path
from .views import CustomerAnalysisView

app_name = 'customers'

urlpatterns = [
    path('analyze/', CustomerAnalysisView.as_view(), name='analyze_customer'),
]
