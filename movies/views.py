from django.db.models import Count, Q
from django.http import JsonResponse
from django.http.response import HttpResponse
from django.shortcuts import render
from django.urls.base import reverse
from django.views.generic import ListView, DetailView, FormView, TemplateView
from django.views.generic.base import View
from django.views.generic.detail import SingleObjectMixin
from django.views import View

from .models import People, Genre, Movie, CastAndCrew, Review
from .forms import ReviewForm


class MovieListView(ListView):

    model = Genre
    context_object_name = 'genre_list'
    template_name = 'movie_list.html'

    def get_queryset(self):

        return Genre.objects.annotate(review_count=Count('movies__reviews')).order_by('-review_count')[:10]

class GenreListView(ListView):

    model = Genre
    context_object_name = 'genre_list'
    template_name = 'genre_list.html'
    ordering = ['genre']

class GenreDetailView(DetailView):

    model = Genre
    context_object_name = 'genre'
    template_name = 'genre_detail.html'

class MovieDetailView(DetailView):

    model = Movie
    context_object_name = 'movie'
    template_name = 'movie_detail.html'

    def get_context_data(self, **kwargs): 
        context = super(MovieDetailView, self).get_context_data(**kwargs)
        context['review_form'] = ReviewForm()
        context['reviews'] = self.get_object().reviews.all().order_by('-date_posted')
        return context

class ReviewFormView(SingleObjectMixin, FormView):

    template_name = 'movie_detail.html'
    form_class = ReviewForm
    model = Movie

    def post(self, request, *args, **kwargs):
        
        if not request.user.is_authenticated:
            return HttpResponse('You must be logged in to review.')
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        
        form.instance.author = self.request.user
        form.instance.movie = self.object
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        
        return reverse('movie_detail', args=[str(self.object.id)])

class MovieHybridView(View):

    def get(self, request, *args, **kwargs):
        
        view = MovieDetailView.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        
        view = ReviewFormView.as_view()
        return view(request, *args, **kwargs)

class PeopleDetailView(DetailView):

    model = People
    context_object_name = 'people'
    template_name = 'people_detail.html'

def fetch_get(request):

    movies = Movie.objects.annotate(review_count=Count('reviews')).order_by('-review_count')
    people = People.objects.all().order_by('name')
    genres = Genre.objects.all().order_by('genre')
    data = {
        'movies': [],
        'people': [],
        'genres': []
    }
    for movie in movies:
        avg_review = movie.avg_review
        data['movies'].append({
            'title': movie.title,
            'link': movie.get_absolute_url(),
            'cover': movie.cover.url,
            'date_released': movie.date_released,
            'avg_review': avg_review,
            'movie_rated':movie.movie_rated,
            'distribution_company':movie.distribution_company
        })
    for person in people:
        data['people'].append({
            'name': person.name,
            'link': person.get_absolute_url(),
            'picture': person.picture.url,
            'birth_date': person.birth_date,
            'birth_place': person.birth_place
        })
    for genre in genres:
        data['genres'].append({
            'genre': genre.genre,
            'link': genre.get_absolute_url()
        })
    return JsonResponse(data)

class SearchView(TemplateView):

    template_name = 'search_list.html'

    def get_context_data(self, **kwargs):
        
        context = {}
        search = self.request.GET.get('search')
        context['search_string'] = search
        context['movie_list'] = Movie.objects.filter(
                                Q(title__icontains=search) |
                                Q(distribution_company__icontains=search) |
                                Q(crew__person__name__icontains=search) |
                                Q(crew__role__icontains=search) |
                                Q(genre__genre__icontains=search)
                                ).distinct().order_by('title')
        context['people_list'] = People.objects.filter(
                                 Q(name__icontains=search) |
                                 Q(roles__role__icontains=search) |
                                 Q(roles__movie__title__icontains=search)
                                 ).distinct().order_by('name')
        context['genre_list'] = Genre.objects.filter(
                                Q(genre__icontains=search) |
                                Q(movies__title__icontains=search)
                                ).distinct().order_by('genre')
        return context