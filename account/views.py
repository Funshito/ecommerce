from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegistrationForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('e-commerce-app:product')
        else:
            messages.error(request, 'Username or Password invalid')
    return render(request, 'account/login.html')

def register(request):
    if request.method == 'POST':
        register = RegistrationForm(request.POST)
        if register.is_valid():
            register.save()
            messages.success(request, 'Registration successfully')
            return redirect('account:login')
    else: 
        register = RegistrationForm()
    context = {
        'register': register
    }
     
    return render(request, 'account/register.html', context)