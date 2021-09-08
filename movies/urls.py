from django.urls import path

from .views import (
                MovieListView, 
                GenreListView, 
                GenreDetailView, 
                MovieHybridView, 
                PeopleDetailView, 
                SearchView,
                fetch_get,
)


urlpatterns = [
    path('', MovieListView.as_view(), name='movie_list'),
    path('genre/', GenreListView.as_view(), name='genre_list'),
    path('<uuid:pk>/', MovieHybridView.as_view(), name='movie_detail'),
    path('people/<uuid:pk>/', PeopleDetailView.as_view(), name='people_detail'),
    path('genre/<uuid:pk>/', GenreDetailView.as_view(), name='genre_detail'),
    path('search/', SearchView.as_view(), name='search_list'),
    path('fetch23755/', fetch_get, name='fetch'),
]