from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
 path('signup/', views.signup, name='signup'),
 path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
 path('login/', views.login, name='login'),
]