from django.shortcuts import render, redirect
from .models import Agent
from .forms import RegistrationForm, LoginForm
from django.contrib.auth import authenticate, login
# Create your views here.
def index(request):
    
    return render(request, "app/index.html")

def leads(request):
    agents = Agent.objects.all()
    context = {'agents':agents}
    return render(request, "app/team_leads.html", context)


def register_view(request):
    msg = None
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = "user created"
            return redirect('login')
        else:
            msg = "form is not valid"
    else:
        form = RegistrationForm()
    return render(request, "app/register.html", {'form':form, 'msg':msg})

def login_view(request):
    msg = None
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
            else:
                msg = "Invalid credentials"
        else:
            msg = "error validation"
    return render(request, "app/login.html", {'form':form, 'msg':msg})
