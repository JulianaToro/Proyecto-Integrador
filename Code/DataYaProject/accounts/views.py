from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.contrib.auth.views import LoginView
from .forms import CustomAuthenticationForm
from django.contrib.auth import authenticate, login


# Vista Sing Up
def singupaccount(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'singupaccount.html', {'form': form})

# Vista Login
def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')

    else:
        form = CustomAuthenticationForm()
    return render(request, 'loginaccount.html', {'form': form})
