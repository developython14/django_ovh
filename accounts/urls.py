from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login_view, name='login'),
    path('signup', views.signup, name='signup'),
    path('test_user', views.test, name='test'),
    path('dash', views.dash, name='dash'),
    path('logout', views.logoutview, name='logout'),
    path('room', views.main_view, name='room'),
    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',  
        views.activate, name='activate'),  
]
