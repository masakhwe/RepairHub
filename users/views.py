from django.shortcuts import render, redirect
from django.contrib.auth.models import User


def register(request):
    if request.method == 'POST':
        user_name = request.POST.get('username')
        e_mail = request.POST.get('email')
        pass_word = request.POST.get('password')

        User.objects.create(username=user_name, email=e_mail, password=pass_word)
        return redirect('login')

    return render(request, 'users/register.html')


def login(request):
    return render(request, 'users/login.html')
