from django.db import models
from django.contrib.auth.models import AbstractUser

# Representar Usuarios
class CustomUser(AbstractUser):
    USERNAME_FIELD = 'email'

    ROLES = [
    ('Analista de datos', 'Analista de datos'),
    ('Gerente de BI', 'Gerente de BI'),
    ('Analista de ventas', 'Analista de ventas'),
    ('Gerente de producto', 'Gerente de producto'),
    ('Administrador', 'Administrador'),
    ('CEO', 'CEO'),
    ]
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    company_name = models.CharField(max_length=100)
    role = models.CharField(max_length=2, choices=ROLES)
