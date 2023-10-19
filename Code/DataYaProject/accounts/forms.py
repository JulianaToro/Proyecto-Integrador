from django import forms
from .models import CustomUser
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import AuthenticationForm
import re


# Formulario de registro
class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'name', 'last_name', 'company_name', 'role']

    # Verificar campos en blanco
    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        last_name = cleaned_data.get('last_name')
        email = cleaned_data.get('email')
        company_name = cleaned_data.get('company_name')
        role = cleaned_data.get('role')
        password = cleaned_data.get('password')

        if not name or not last_name or not email or not company_name or not role or not password:
            raise ValidationError("Todos los campos son obligatorios.")

        if len(name) < 4 or len(last_name) < 4 or len(company_name) < 4:
            raise ValidationError("El nombre, el apellido y el nombre de la compañia deben tener al menos 4 caracteres.")

        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise ValidationError("El correo electronico no es válido")
        
        if len(password) < 8:
            raise ValidationError("La contraseña debe tener al menos 8 caracteres.")

    # Email repetido    
    error_messages = {
            'email': {
                'unique': "El correo electrónico ya está registrado.",
            },
        }

# Formulario de autenticación
class CustomAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(label='Email')