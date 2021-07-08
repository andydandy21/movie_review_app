from django.db.models import Avg
from django.http.response import HttpResponseForbidden
from django.shortcuts import render
from django.urls.base import reverse
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.base import View
from django.views.generic.detail import SingleObjectMixin
from django.views import View

from .models import People, Genre, Movie, CastAndCrew, Review
from .forms import ReviewForm


class MovieListView(ListView):

    model = Movie
    context_object_name = 'movie_list'
    template_name = 'movie_list.html'

class MovieDetailView(DetailView):

    model = Movie
    context_object_name = 'movie'
    template_name = 'movie_detail.html'

    def get_context_data(self, **kwargs): 
        context = super(MovieDetailView, self).get_context_data(**kwargs)
        context['review_form'] = ReviewForm()
        context['reviews'] = self.get_object().reviews.all().order_by('-date_posted')
        context['review_avg'] = self.get_object().reviews.aggregate(Avg('viewer_rating'))
        return context

class ReviewFormView(SingleObjectMixin, FormView):

    template_name = 'movie_detail.html'
    form_class = ReviewForm
    model = Movie

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden
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