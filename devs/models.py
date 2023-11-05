from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Dev(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    age = models.PositiveIntegerField(blank=True, validators=[MinValueValidator(10), MaxValueValidator(100)])
    country = models.CharField(blank=True, max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)