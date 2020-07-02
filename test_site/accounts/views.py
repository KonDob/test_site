from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from .models import UserAccount
from django.utils import timezone
from django.contrib import messages


# Create your views here.
def indexView(request):
    return render(request, 'index.html')

@login_required
def dashboardView(request):
    users = User.objects.values_list('username', flat = True)
    
    #TODO write function to determine is user is online
    #TODO also remove extra symbols
    return render(request, 'dashboard.html', {'users': users})

def registerView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    else:
        form = UserCreationForm()
    
    return render(request,'registration/register.html', {'form':form})

def status_info(request):
    return render(request, 'status_info.html')

def change_status(request):
    #TODO change value of current user status
    if request.method == "POST":
        if request.user.useraccount.status:
            request.user.useraccount.toggle_status()
            btn_status = 'Online'
        else:
            request.user.useraccount.toggle_status()
            btn_status = 'Offline'
            
    return render(request, 'status_info.html', {'status': btn_status})
    