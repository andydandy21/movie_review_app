from django.shortcuts import render
from django.views.generic import ListView

from .models import People, Genre, Movie, CastAndCrew, Review


class MovieListView(ListView):

    model = Movie
    context_object_name = 'movie_list'
    template_name = 'movie_list.html'
