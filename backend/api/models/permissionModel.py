"""
Feature/Permission Model:
This model is used to define and manage features or permissions.
"""
from django.db import models

class Permission(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name
