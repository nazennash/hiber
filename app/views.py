from django.shortcuts import render, redirect
from .forms import LoginForm, RegistrationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import UserForm, CreateLead, CreateAgent
from django.contrib.auth.decorators import login_required
from .decorators import administrator_required, agent_required, lead_required
from .models import User, Agent, Lead

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

def logout_view(request):
    logout(request)
    return render(request, "app/logout.html")

@administrator_required
def administrator_index(request):

    agent_list = Agent.objects.all().order_by('-id')
    agent_list_count = agent_list.count()

    
    context = {'agent_list':agent_list, 'agent_list_count':agent_list_count}
    return render(request, "app/admin_index.html", context)

@administrator_required
def add_agent(request):

    form = CreateAgent()
    if request.method == "POST":
        form = CreateAgent(request.POST)
        if form.is_valid():
            agent_name = form.cleaned_data['agent']
            try: 
                Agent.objects.get(user=agent_name)
                messages.warning(request, "user exists")
            except Agent.DoesNotExist:
                agent = Agent.objects.create(
                    user = agent_name
                )
                messages.success(request, "User created Successfully")
                return redirect('administrator')
                
        else:
            messages.warning(request, "Invalid Request")

    context = {'form':form}
    return render(request, "app/add_agent.html", context)

@agent_required
def agent_index(request):
    form = CreateLead()
    if form.is_valid():
        print(form.cleaned_data)
    context = {'form':form}
    return render(request, "app/agent_index.html", context)

@lead_required
def lead_index(request):
    return render(request, "app/lead_index.html")
