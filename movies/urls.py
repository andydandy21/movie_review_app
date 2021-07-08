from django.urls import path

from .views import MovieListView, MovieHybridView, PeopleDetailView


urlpatterns = [
    path('', MovieListView.as_view(), name='movie_list'),
    path('<uuid:pk>/', MovieHybridView.as_view(), name='movie_detail'),
    path('people/<uuid:pk>/', PeopleDetailView.as_view(), name='people_detail'),
]