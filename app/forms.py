from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import User, Agent, Lead

class LoginForm(forms.Form):
    username = forms.CharField(label="Username",widget=forms.TextInput(attrs={'class':'border rounded px-2 w-[400px] h-[38px] mx-auto'}))
    password = forms.CharField(label="Password",widget=forms.PasswordInput(attrs={'class':'border rounded px-2 w-[400px] h-[38px] mx-auto'}))

    class Meta:
        model = User
        fields = ['username', 'password']

class RegistrationForm(UserCreationForm):
    username = forms.CharField(label="Username", widget=forms.TextInput(attrs={'class':'border rounded px-2 w-[400px] h-[38px] mx-auto'}))
    password1 = forms.CharField(label="Password",widget=forms.PasswordInput(attrs={'class':'border rounded px-2 w-[400px] h-[38px] mx-auto'}))
    password2 = forms.CharField(label="Confirm Password",widget=forms.PasswordInput(attrs={'class':'border rounded px-2 w-[400px] h-[38px] mx-auto'}))
    email = forms.CharField(label="Email",widget=forms.EmailInput(attrs={'class':'border rounded px-2 w-[400px] h-[38px] mx-auto'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'is_admin', 'is_agent', 'is_lead')
    


class UserForm(forms.ModelForm):
    agent = forms.ModelChoiceField(queryset=User.objects.filter(is_agent=True), empty_label=None, label="Agent")

    class Meta:
        model = User
        fields = ['agent']

class CreateLead(forms.ModelForm):
    agent_search = User.objects.filter(is_lead=True)
    name = forms.ModelChoiceField(queryset=agent_search, empty_label=None, label="Lead Name")
    class Meta:
        model = User
        fields = ['name']

class CreateAgent(forms.ModelForm):
    agent = forms.ModelChoiceField(queryset=User.objects.filter(is_agent=True), empty_label=None, label="Agent")
    
    class Meta:
        model = User
        fields = ['agent']
    