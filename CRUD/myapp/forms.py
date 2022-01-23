from django import forms
from django.forms import fields
from .models import User
from django.core import validators


class Studentregi(forms.ModelForm):
    class Meta:
        model = User
        fields = ['studentname','bookname','booknumber']
        widgets = {
            'studentname':forms.TextInput(attrs={'class':'form-control'}),
            'bookname':forms.TextInput(attrs={'class':'form-control'}),
            'booknumber':forms.TextInput(attrs={'class':'form-control'})
        }
