#views are python functions that takes user requests and 
#returns requests/html.

from django.shortcuts import render, get_object_or_404
from .models import Album


#all_albums will connect to database and get all objects available and
#display results on the music page
def index(request):
    all_albums = Album.objects.all()
    return render(request, 'music/index.html', {'all_albums': all_albums})

def detail(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    return render(request, 'music/detail.html', {'album': album})