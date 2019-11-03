from django.db import models
from django.contrib.auth.models import User
from django import forms


# Create your models here.
class Worksite(models.Model):
    """ Add New Worksite Form """
    name = models.CharField(max_length=150)
    shift = models.CharField(max_length=255)
    buffer_time = models.TimeField()
    cutoff_time = models.TimeField()
    contact_no = models.CharField(max_length=12)
    address = models.TextField()
    device = models.CharField(max_length=255)

    class meta:
        model = 'Worksite'
        fields = '__all__'
