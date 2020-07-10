#".": the period points to the current directory

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]