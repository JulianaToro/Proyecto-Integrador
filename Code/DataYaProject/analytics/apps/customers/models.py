from django.db import models

class Customer(models.Model):
    # Define los campos relevantes para tu base de datos de clientes
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    # Puedes agregar más campos según tus necesidades

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
