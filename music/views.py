#views are python functions that takes user requests and 
#returns requests/html.

from django.http import HttpResponse
from .models import Album

#all_albums will connect to database and get all objects available and
#display results on the music page
def index(request):
    all_albums = Album.objects.all()
    html = ''
    for album in all_albums:
        path = '/music/' + str(album.id) + '/'
        html += '<a href="' + path + '">' + album.album_title + '</a><br>'
    return HttpResponse(html)

def detail(request, album_id):
    return HttpResponse("<h2>Details for Album id: " + str(album_id) + " </h2>")
