from django.shortcuts import render, redirect, get_object_or_404
from .forms import LoginForm
from django.contrib import messages
from django.contrib.auth.models import User, auth
# Create your views here.
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('business:index')
        else:
            messages.info(request, 'Invalid username or password')
            return redirect('authz:login')

    return render(request, "authz/login.html")

def logout(request):
    auth.logout(request)
    return redirect('/')

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']

        if password == confirm_password:
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email already exist")
                return redirect('authz:signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, "Username already exist")
                return redirect('authz:signup')
            else:
                user = User.objects.create_user(
                    username=username, first_name=first_name, last_name=last_name, email=email, password=password)
                user.save()
                messages.info(request, "Account created")
                return redirect('authz:login')
        else:
            messages.info(request, "Password didnt match")
            return redirect('authz:signup')
    return render(request, "authz/signup.html")
