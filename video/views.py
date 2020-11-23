from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

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


def SignUp(request):
    context = ''
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        email = request.POST.get('email', None)
        form = RegisterForm(request.POST)

        if form.is_valid():
            existUser = authenticate(username=username, password=password)
            if existUser:
                context = 'user already exist.'
            else:
                user = User.objects.create_user(username, email, password)
                user.save()
                return redirect('/')
    else:
        form = RegisterForm()
    return render(request, 'video/register.html', {
    'form':form, 'context':context
})