"""
Payment Model:
Store information related to user payments, invoices,
transaction details, or billing history.
"""
from django.db import models
from django.contrib.auth.models import User

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    # Add additional fields as per your requirements
    # ...

    def __str__(self):
        return f"Payment #{self.id} - User: {self.user.username}, Amount: {self.amount}"
