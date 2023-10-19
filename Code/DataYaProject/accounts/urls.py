from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
 path('signupaccount/', views.signupaccount, name='signupaccount'),
 path('logout/', LogoutView.as_view(next_page='loginaccount'), name='logoutaccount'),
 path('login/', views.loginaccount, name='loginaccount'),
]