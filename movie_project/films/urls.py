"""
from . import views
urlpatterns = [
    path('', views.index)
]"""

from django.urls import path
from .views import movie_create_view, movie_list_view

urlpatterns = [
    path('', movie_create_view, name='movie_create'),
    path('movie_list/', movie_list_view, name='movie_list'),
]
