from django.shortcuts import render, redirect
from .forms import LoginForm, RegistrationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def index(request):
    return render(request, "app/index.html")
    
#authentications

def login_view(request):

    if request.user.is_authenticated:
        return redirect('index')
    
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None and user.is_admin:
                login(request, user)
                return redirect('administrator')
            if user is not None and user.is_agent:
                login(request, user)
                return redirect('agent')
            if user is not None and user.is_lead:
                login(request, user)
                return redirect('lead')
            else:
                print('two')
                form.add_error(None, "Invalid username or password")
    else:
        print('one')
        form = LoginForm()
    return render(request, "app/login.html", {'form': form})

def registration_view(request):
    if request.user.is_authenticated:
        return redirect('index')
    
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # user.save()
            return redirect('login')
        else:
            print('invalid')
    else:
        form = RegistrationForm()
    context = {'form':form}

    return render(request, "app/register.html", context)

def logout(request):
    user = request.user
    logout(request, user)

def administrator_index(request):
    return render(request, "app/admin_index.html")

def agent_index(request):
    return render(request, "app/agent_index.html")

def lead_index(request):
    return render(request, "app/lead_index.html")