from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('main:index')
        else:
            raise ValidationError('username 또는 password가 틀립니다.')
            return redirect('main:index')
    else:
        return render(request, 'main/index.html')


def signup(request):
    username = request.POST['username']
    password = request.POST['password']
    users = User.objects.all()

    if users.filter(username=username):
        return HttpResponse('이미 사용중인 username 입니다.')
    else:
        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        return render(request, 'main/index.html')


def signout(request):
    logout(request)
    return redirect('main:index')
