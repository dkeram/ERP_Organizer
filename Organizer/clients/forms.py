from django import forms
from .models import Clients
from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Clients
        fields = ['sirname', 'name','vat','phone','email','address','user_name','password']


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields =['username','email','password']
