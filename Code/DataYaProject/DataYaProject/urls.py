from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('analytics/', include('analytics.urls')),
    path('reports/', include('reports.urls')),
    path('dashboards/', include('dashboards.urls')),
    path('firstanalysis/', include('firstanalysis.urls')),
]


