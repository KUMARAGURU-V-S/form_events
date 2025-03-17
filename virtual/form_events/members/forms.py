# myapp/forms.py
from django import forms

class LoginForm(forms.Form):
    name = forms.CharField(max_length=100, label='You Name')
    password = forms.CharField(widget=forms.PasswordInput, label='Password')
