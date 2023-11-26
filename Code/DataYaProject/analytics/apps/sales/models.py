from django.db import models

from django.db import models

class Sale(models.Model):
    # Define los campos relevantes para tu base de datos de ventas
    date = models.DateField()
    product_name = models.CharField(max_length=255)
    quantity = models.IntegerField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    # Puedes agregar más campos según tus necesidades

    def __str__(self):
        return f"{self.date} - {self.product_name}"
