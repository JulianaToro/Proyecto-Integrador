from django.db import models

class AnalysisReport(models.Model):
    excel_file = models.FileField(upload_to='excel_files/')
    mae = models.FloatField()
