#views are python functions that takes user requests and 
#returns requests/html.

from django.http import HttpResponse
#from django.template import loader
from django.shortcuts import render
from .models import Album


#all_albums will connect to database and get all objects available and
#display results on the music page
def index(request):
    all_albums = Album.objects.all()
    #template = loader.get_template('music/index.html')
    
    context= {'all_albums': all_albums}
    #return HttpResponse(template.render(context, request))

    return render(request, 'music/index.html', context)

def detail(request, album_id):
    return HttpResponse("<h2>Details for Album id: " + str(album_id) + " </h2>")
