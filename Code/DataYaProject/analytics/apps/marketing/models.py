from django.db import models

class MarketingCampaign(models.Model):
    # Define los campos relevantes para tu base de datos de marketing
    campaign_name = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    # Puedes agregar más campos según tus necesidades

    def __str__(self):
        return self.campaign_name

