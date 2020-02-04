from django.contrib.auth import authenticate, login
from django.core.exceptions import ValidationError
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
            return redirect('base')
    else:
        return render(request, 'main/index.html')
