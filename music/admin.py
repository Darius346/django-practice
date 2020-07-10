#Makes changes to admin page

from django.contrib import admin
from .models import Album
admin.site.register(Album)