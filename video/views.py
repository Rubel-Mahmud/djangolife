from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from video.models import video

from video.forms import *

def index(request):
    songs = video.objects.all().order_by('-id')
    return render(request, 'video/index.html', {
        'songs':songs,
    })

def SignIn(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        form = LoginForm(request.POST)

        if form.is_valid():
            user = authenticate(username=username, password=password)
            if user:
                return HttpResponseRedirect('/')
            else:
                return HttpResponse('username or password is incorrect.')
    else:
        form = LoginForm()
    return render(request, 'video/login.html', {
        'form':form,
})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'user created successfully')
            return HttpResponseRedirect('/login/')
    else:
        form = UserCreationForm()
    return render(request, 'video/register.html', {
        'form':form,
    })