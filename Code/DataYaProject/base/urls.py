from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('Accounts.urls')),
    path('analytics/', include('analytics.urls')),
    path('reports/', include('Accounts.urls')),
]


