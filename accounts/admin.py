from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from .models import Person

admin.site.register(Person)

admin.site.site_header = "INREPM Admin"
admin.site.index_title = "Welcome to INternational REsearch PlatforM adminstartion"
admin.site.site_title = "INREPM Admin"