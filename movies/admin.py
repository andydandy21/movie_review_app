from django.contrib import admin

from .models import People, Genre, Movie, CastAndCrew, Review


class CastAndCrewInline(admin.TabularInline):

    model = CastAndCrew
    extra = 1

class ReviewInline(admin.TabularInline):
    
    model = Review
    extra = 1

class RolesInline(admin.TabularInline):

    model = CastAndCrew
    extra = 1
    verbose_name = 'Role'
    verbose_name_plural = 'Roles'

class PeopleAdmin(admin.ModelAdmin):

    inlines = [
        RolesInline
    ]

class MovieAdmin(admin.ModelAdmin):
    
    fields = (
        'title',
        'production_company',
        'distribution_company',
        'date_released',
        'movie_rated',
        'movie_length',
        'plot',
        'genre'
    )
    filter_horizontal = ('genre',)
    inlines = [
        CastAndCrewInline, ReviewInline,
    ]


admin.site.register(People, PeopleAdmin)
admin.site.register(Genre)
admin.site.register(Movie, MovieAdmin)