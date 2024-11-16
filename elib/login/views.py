from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('homepage:home')
        else:
            messages.error(request, 'Неверное имя пользователя или пароль.')

    return render(request, 'login/login.html')