from django import forms
from .models import Link
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class MyModelForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = ['link', 'urgency', 'id']

class SigningForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2') # I edited here a little