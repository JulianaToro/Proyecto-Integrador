from django.db import models

class FinancialData(models.Model):
    # Define los campos relevantes para tu base de datos financiera
    year = models.IntegerField()
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    investments = models.DecimalField(max_digits=10, decimal_places=2)
    # Puedes agregar más campos según tus necesidades

    def __str__(self):
        return f"{self.year} - Budget: {self.budget}, Investments: {self.investments}"
