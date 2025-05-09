import datetime

from django.db import models
from django.utils import timezone

class Artist(models.Model):
    name_first = models.CharField(max_length=100)
    name_last = models.CharField(max_length=100)
    name_display = models.CharField(max_length=200)
      
    def __str__(self):
        return self.name_display
    
    
    
