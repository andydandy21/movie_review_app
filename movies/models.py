import uuid
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils import timezone


class People(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200, verbose_name='Name')
    birth_date = models.DateField(blank=True, null=True, verbose_name='Birthday')
    birth_place = models.CharField(max_length=200, blank=True, verbose_name='Birthplace')
    biography = models.TextField(max_length=5000, blank=True, verbose_name='Bio')
    picture = models.ImageField(upload_to='people_pictures/', default='default.png')

    class Meta:

        verbose_name_plural = 'People'

    def __str__(self):

        return self.name

class Genre(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    genre = models.CharField(max_length=200, unique=True, verbose_name='Genre')

    def __str__(self):

        return self.genre

class Movie(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200, verbose_name='Title')
    production_company = models.CharField(max_length=200, blank=True, verbose_name='Production Company')
    distribution_company = models.CharField(max_length=200, blank=True, verbose_name='Distributed By')
    date_released = models.DateField(default=None, blank=True, null=True, verbose_name='Release Date')
    genre = models.ManyToManyField(Genre, blank=True, related_name='movies', verbose_name='Genre')
    movie_rated = models.CharField(max_length=5, blank=True, verbose_name='Rated')
    movie_length = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(51420)], blank=True, null=True, verbose_name='Running Time')
    plot = models.TextField(max_length=5000, blank=True, verbose_name='Plot')
    cover = models.ImageField(upload_to='movie_covers/', default='default.png')

    def __str__(self):

        return self.title

class CastAndCrew(models.Model):
    
    role = models.CharField(max_length=200, verbose_name='Role')
    person = models.ForeignKey(People, on_delete=models.CASCADE, related_name='roles')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='crew')

    class Meta:

        verbose_name = 'Cast and Crew'
        verbose_name_plural = 'Cast and Crew'

    def __str__(self):

        return self.role

class Review(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='reviews', verbose_name='User')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews', verbose_name='Movie')
    viewer_rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)], verbose_name='Viewer Rating')
    title = models.CharField(max_length=60, blank=True)
    comment = models.TextField(max_length=300, blank=True)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):

        return self.title
