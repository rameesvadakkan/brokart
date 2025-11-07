from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages, auth

# Create your views here.

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm = request.POST['confirm']
        if password == confirm:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already taken')
            else:
                User.objects.create_user(username=username, email=email, password=password)
                messages.success(request, 'Account created! You can log in now.')
                return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
    return render(request, 'accounts/register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            return redirect('product_list')
        else:
            messages.error(request, 'Invalid credentials')
    return render(request, 'accounts/login.html')

def logout_view(request):
    auth.logout(request)
    return redirect('login')
