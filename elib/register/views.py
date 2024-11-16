from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages


def register_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Пользователь с таким именем уже существует.')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Пользователь с таким email уже существует.')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('login:login')
        else:
            messages.error(request, 'Пароли не совпадают.')

    return render(request, 'register/register.html')
