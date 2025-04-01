from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView

from video_security_app.models import Video

def home(request):
    videos = Video.objects.all()
    return render(request, 'home.html', {'videos': videos})

def deletevideo(request,video_id):
    if request.user.is_authenticated and request.user.is_staff:
        video = get_object_or_404(Video,pk=video_id)
        video.delete()
    else:
        return HttpResponse("you can only view")
    
    next_url = request.GET.get('next', '/')
    return redirect(next_url)

class MyLoginView(LoginView):
    template_name = "login.html"
    authentication_form = AuthenticationForm
    redirect_authenticated_user = True
    next_page = '/' 

def live_stream(request):
    stream_url = "http://pendelcam.kip.uni-heidelberg.de/mjpg/video.mjpg"
    stream_url2 = "http://67.53.46.161:65123/mjpg/video.mjpg"
    stream_url3 = "http://77.222.181.11:8080/mjpg/video.mjpg"
    return render(request, "stream.html", {"stream_url": stream_url,"stream_url2":stream_url2,"stream_url3":stream_url3})

