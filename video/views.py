from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

from video.models import video

from video.forms import *

def index(request):
    songs = video.objects.all().order_by('-id')
    return render(request, 'video/index.html', {
        'songs':songs,
    })

def SignIn(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        user = form.authenticate()

        if user:
            return redirect('/')
        else:
            return HttpResponse('Login failed or invalid password')
    else:
        form = LoginForm()
    return render(request, 'video/login.html',{
        'form':form,
    })


def Register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user:
                return HttpResponse("User created " + str(user.id) + " succesfully.")
            else:
                return HttpResponse("Registration failed.")
    else:
        form = UserCreationForm()

    return render(request, 'video/register.html', {
        'form':form,
    })