#from django.db import models

# Create your models here.
from django.db import models

class Book(models.Model):
    objects = None
    r_name = models.CharField(max_length=100)
    r_address = models.CharField(max_length=100)
    r_status = models.CharField(max_length=100)
    publication_date = models.DateField()
