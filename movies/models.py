from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils import timezone


class Crew(models.Model):
    
    name = models.CharField(max_length=200, verbose_name='Name')
    birth_date = models.DateField(verbose_name='Birthday')
    birth_place = models.CharField(max_length=200, verbose_name='Birthplace')
    biography = models.TextField(max_length=5000, verbose_name='Bio')

    def __str__(self):

        return self.name

class Genre(models.Model):
    
    genre = models.CharField(max_length=200, unique=True, verbose_name='Genre')

    def __str__(self):

        return self.genre

class Movie(models.Model):

    title = models.CharField(max_length=200, verbose_name='Title')
    production_company = models.CharField(max_length=200, verbose_name='Production Company')
    distribution_company = models.CharField(max_length=200, verbose_name='Distributed By')
    date_released = models.DateField(verbose_name='Release Date')
    genre = models.ManyToManyField(Genre, related_name='movies', verbose_name='Genre')
    movie_rated = models.CharField(max_length=5, verbose_name='Rated')
    movie_length = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(51420)], verbose_name='Running Time')
    plot = models.TextField(max_length=5000, verbose_name='Plot')
    crew = models.ManyToManyField(Crew, related_name='movies', verbose_name='Cast and Crew')

    def __str__(self):

        return self.title

class Role(models.Model):
    
    name = models.CharField(max_length=200, verbose_name='Role')
    crew = models.ForeignKey(Crew, on_delete=models.CASCADE, related_name='roles')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='roles')

    def __str__(self):

        return self.name

class Review(models.Model):

    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='reviews', verbose_name='User')
    viewer_rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)], verbose_name='Viewer Rating')
    title = models.CharField(max_length=60)
    comment = models.TextField(max_length=300)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):

        return self.title
