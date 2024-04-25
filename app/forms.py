from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import User

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'border rounded px-3'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'border rounded px-3'}))

    class Meta:
        model = User
        fields = ['username', 'password']

class RegistrationForm(UserCreationForm):
    username = forms.CharField(label="Username", widget=forms.TextInput(attrs={'class':'border rounded px-3'}))
    password1 = forms.CharField(label="Password",widget=forms.PasswordInput(attrs={'class':'border rounded px-3'}))
    password2 = forms.CharField(label="Confirm Password",widget=forms.PasswordInput(attrs={'class':'border rounded px-3'}))
    email = forms.CharField(label="Email",widget=forms.EmailInput(attrs={'class':'border rounded px-3'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'is_admin', 'is_agent', 'is_lead')
    