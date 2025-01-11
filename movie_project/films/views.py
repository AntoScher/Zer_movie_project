"""
from django.http import HttpResponse
def index(request):
    return HttpResponse("<h1>Это  проект movie_project созданный на Django</h1>")
"""

from django.shortcuts import render, redirect
from .models import Movie
from .forms import MovieForm

def movie_create_view(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('movie_list')
    else:
        form = MovieForm()
    return render(request, 'movie_create.html', {'form': form})

def movie_list_view(request):
    movies = Movie.objects.all()
    return render(request, 'movie_list.html', {'movies': movies})
