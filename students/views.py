from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import loginForm
from .models import Students


# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        print(user)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Welcome')
            return redirect('dashboard')
        else:
            messages.error(request, 'Username or Password not found')
            return render(request, 'user/login.html', {'form': loginForm()})

    else:
        return render(request, 'user/login.html', {'form': loginForm()})


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
    messages.success(request, 'You Have Signed Out')
    return redirect('index')


def dashboard(request):
    return render(request, 'student/dashboard.html')
