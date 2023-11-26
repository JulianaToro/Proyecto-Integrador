from django.urls import path
from .views import MarketingAnalysisView

app_name = 'marketing'

urlpatterns = [
    path('analyze/', MarketingAnalysisView.as_view(), name='analyze_marketing'),
]
