from django.db import models

class CalculationHistory(models.Model):
    monthly_investment = models.DecimalField(max_digits=10, decimal_places=2)
    yearly_rate = models.DecimalField(max_digits=5, decimal_places=2)
    years = models.IntegerField()
    future_value = models.DecimalField(max_digits=15, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"${self.future_value} - {self.created_at}"
