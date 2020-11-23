from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate

from video.models import video

def index(request):
    songs = video.objects.all().order_by('-id')
    return render(request, 'video/index.html', {
        'songs':songs,
    })

def SignIn(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        if username is not None and password is not None :
            user = authenticate(username=username, password=password)
            if user:
                return redirect('/')
            else:
                return HttpResponse('login failed')
        else:
            return HttpResponse('Empty value entered.')
    return render(request, 'video/login.html')
