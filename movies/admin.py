from django.contrib import admin

from .models import People, Genre, Movie, CastAndCrew, Review


class CastAndCrewInline(admin.TabularInline):

    model = CastAndCrew
    extra = 1
    autocomplete_fields = ('person', )

class ReviewInline(admin.TabularInline):
    
    model = Review
    extra = 1

class RolesInline(admin.TabularInline):

    model = CastAndCrew
    extra = 1
    verbose_name = 'Role'
    verbose_name_plural = 'Roles'
    autocomplete_fields = ('movie', )
    

class PeopleAdmin(admin.ModelAdmin):

    search_fields = ['name']
    list_display = ['name', 'birth_date', 'birth_place',]
    inlines = [
        RolesInline
    ]

class MovieAdmin(admin.ModelAdmin):
    
    fields = (
        'title',
        'cover',
        'production_company',
        'distribution_company',
        'date_released',
        'movie_rated',
        'movie_length',
        'plot',
        'genre'
    )
    filter_horizontal = ('genre',)
    search_fields = ['title']
    list_display = ['title', 'movie_rated', 'date_released', 'movie_length', ]
    inlines = [
        CastAndCrewInline, ReviewInline,
    ]
    
    
admin.site.register(People, PeopleAdmin)
admin.site.register(Genre)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Review)