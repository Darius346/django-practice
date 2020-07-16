#views are python functions that takes user requests and 
#returns requests/html.

from django.http import Http404
from django.shortcuts import render
from .models import Album


#all_albums will connect to database and get all objects available and
#display results on the music page
def index(request):
    all_albums = Album.objects.all()
    return render(request, 'music/index.html', {'all_albums': all_albums})

def detail(request, album_id):
    try:
        album = Album.objects.get(pk=album_id)
    except Album.DoesNotExist:
        raise Http404("Album does not exist.")
    return render(request, 'music/detail.html', {'album': album})