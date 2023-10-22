from django.db import models

# Create your models here.
from django.db import models
class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255, blank=True, null=True)
    profession = models.CharField(max_length=255, blank=True, null=True)
    telnumber = models.CharField(max_length=20, blank=True, null=True)

def __str__(self):
    return self.name

