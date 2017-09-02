from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms

from .models import Profile

class SignUpForm(ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'Pin-form--input'}), max_length=10)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'Pin-form--input'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'Pin-form--input'}))

    class Meta:
        model = User
        fields = ('email', 'username', 'password')

class LogInForm(ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'Pin-form--input'}), max_length=10)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'Pin-form--input'}))

    class Meta:
        model = User
        fields = ('username', 'password')
