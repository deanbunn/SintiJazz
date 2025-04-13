import datetime

from django.db import models
from django.utils import timezone

class Musician(models.Model):
    display_name = models.CharField(max_length=200)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
      
    def __str__(self):
        return self.display_name
    
