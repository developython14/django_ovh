from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Room(models.Model):
    room_name = models.CharField(null=False ,max_length=32)
    USERNAME_FIELD = 'username'

class  Messages(models.Model):
    room = models.ForeignKey(to=Room, on_delete=models.CASCADE)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    message = models.CharField(null=False,max_length = 32)
    USERNAME_FIELD = 'username'
    



    