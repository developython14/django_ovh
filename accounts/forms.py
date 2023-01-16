# accounts/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Person
from crispy_forms.helper import FormHelper
from django.contrib.auth.models import User



class CustomUserCreationForm(forms.ModelForm):
    country_name = forms.CharField(required=True)
    organisme_name = forms.CharField(required=True)
    organisme_website = forms.CharField(required=True)
    organisme_adresse = forms.CharField(required=True)
    accept_contrat = forms.BooleanField(label="En envoyant ce formulaire vous acceptez les Conditions d'utilisation." ,required=True)
    class Meta:
        model = Person
        fields = ('phone' , 'emploi' )


class basecreate(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    class Meta:
        model = User
        fields = ('first_name' , 'last_name' , 'email' , 'username')
        fields_required  =  ('first_name' , 'last_name' , 'email' , 'username')
    



