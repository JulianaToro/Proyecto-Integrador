from django.urls import path
from .views import streamlit_dashboard

app_name = 'analytics'
urlpatterns = [
    path('dashboard/', views.streamlit_dashboard, name='streamlit_dashboard'),
]
