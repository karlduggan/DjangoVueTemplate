"""
Subscription Model:
This model represents the subscription plans or tiers available.
It typically include the following fields:
plan name, description, price, features, duration,
and any associated restrictions or limitations.
"""
from django.db import models

class Subscription(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    duration = models.PositiveIntegerField(help_text="Duration in days")

    # Add additional fields as per your requirements
    # ...

    def __str__(self):
        return self.name
