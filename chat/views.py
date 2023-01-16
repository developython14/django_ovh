from django.shortcuts import render
from accounts.models import *
# Create your views here.

from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    persons = Person.objects.all()
    me = {'username' : request.user.username,
        'first_name':request.user.first_name,
        'last_name':request.user.last_name,
        'email':request.user.email,
    }
    return render(request, "chat/room.html" , {'persons' : persons, 'me':me})



def room(request, room_name):
    return render(request, "chat/chat.html", {"room_name": room_name})



def video(request,room_name):
    return render(request, "chat/peer.html")