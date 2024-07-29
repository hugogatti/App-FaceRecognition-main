from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def login_page(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('listPrescricoes')
        else:
            messages.success(request, 'Invalid username or password')
            redirect('login')
    contexto = {'usuario': request.user}
    return render(request, 'usuarios/login.html', contexto)


def logout_page(request):
    logout(request)
    messages.success(request, 'You are now logged out')
    return redirect('login')