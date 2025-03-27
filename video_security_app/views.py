from django.shortcuts import render

from video_security_app.models import Video

def home(request):
    videos = Video.objects.all()
    return render(request, 'home.html', {'videos': videos})
