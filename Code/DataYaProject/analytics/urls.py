from django.urls import path
from .views import UploadExcelView, database_list

app_name = 'analytics'
urlpatterns = [
    path('upload_excel/', UploadExcelView.as_view(), name='upload_excel'),
    path('databases/', database_list, name='database_list'),
]
