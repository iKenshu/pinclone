from django.forms import ModelForm
from django import forms

from .models import Pin

class PinCreateForm(ModelForm):
    class Meta:
        model = Pin
        fields = ('title', 'image')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'Pin-form--input'}),
            'image': forms.FileInput(attrs={'class': 'Pin-form--file'}),
        }

