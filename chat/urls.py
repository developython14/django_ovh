# chat/urls.py
from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("<str:room_name>/", views.room, name="room"),
    path("screen/video/<str:room_name>/", views.video, name="video"),
    path("webrtc/", views.webrtc, name="webrtc"),
]