from django.db import models
from django.contrib.auth.models import User




User._meta.get_field('email')._unique = True



class Countries(models.Model):
    name = models.CharField(max_length=30 )
    USERNAME_FIELD = 'username'
    
class Organismes(models.Model):
    name = models.CharField(max_length=30 ,unique=True)
    website = models.CharField(max_length=30 ,unique=True)
    adresse = models.CharField(max_length=30 ,unique=True)
    USERNAME_FIELD = 'username'

class Person(models.Model):
    organisme = models.ForeignKey(to=Organismes , on_delete=models.CASCADE)
    accept_contrat = models.BooleanField()
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    country = models.ForeignKey(to=Countries, on_delete=models.CASCADE)
    phone = models.CharField(max_length=30 ,unique=True)
    emploi = models.CharField(max_length=30 ,unique=True)
    USERNAME_FIELD = 'username'
    

