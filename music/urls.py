#".": the period points to the current directory

from django.urls import path
from . import views

app_name = 'music'

urlpatterns = [
    # /music/
    # url(r'^$', views.index, name='index'),
    path('', views.index, name='index'),

    # /music/71/
    # url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail),
    path('<int:album_id>/', views.detail, name='detail'),
]