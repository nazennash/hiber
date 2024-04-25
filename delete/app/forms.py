from django import forms
from .models import Leads, User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={''}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={}))

class RegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={}))
    email = forms.TextInput(widget=forms.EmailField(attrs={}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'is_admin', 'is_agent', 'is_lead')

class LeadForm(forms.ModelForm):
    class Meta:
        model = Leads
        fields = ['first_name']
