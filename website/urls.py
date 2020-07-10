#python manage.py runserver: launchess your website's server
#python manage.py startapp music: creates directory called music
#python manage.py makemigrations music:
#python manage.py migrate:
#python manage.py sqlmigrate music 0001:
#python manage.py shells: takes you to python command line
#urls.py:this serves as a repository for you urls 

from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('music/', include('music.urls')),
]