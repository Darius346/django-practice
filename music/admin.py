#Makes changes to admin page

from django.contrib import admin
from .models import Album, Song

admin.site.register(Album)
admin.site.register(Song)