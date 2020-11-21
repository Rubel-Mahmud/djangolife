from django.shortcuts import render

from video.models import video

def index(request):
    songs = video.objects.all().order_by('-id')
    return render(request, 'video/index.html', {
        'songs':songs,
    });
