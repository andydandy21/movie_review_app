from datetime import datetime, date
from django.contrib.auth import get_user_model
from django.test import TestCase

from .models import (
    Crew,
    Genre,
    Movie,
    Role,
    Review,
)


class MovieTests(TestCase):

    def setUp(self):

        self.user = get_user_model().objects.create_user(
            username='reviewuser',
            email='reviewuser@email.com',
            password='testpass123',
        )
        self.crew = Crew.objects.create(
            name='Will Smith',
            birth_date=date(1968, 9, 25),
            birth_place='Philadelphia, Pennsylvania, U.S.',
            biography='Smith was born on September 25, 1968 in Philadelphia, Pennsylvania to Caroline.',
        )
        self.genre = Genre.objects.create(
            genre='Sci Fi',
        )
        self.movie = Movie.objects.create(
            title='Men in Black',
            production_company='Columbia Pictures, MacDonald Parkes, Amblin Entertainment',
            distribution_company='Sony Pictures Releasing',
            date_released=date(1997, 4, 2),
            movie_rated='PG-13',
            movie_length=98,
            plot='After a government agency makes first contact with aliens in 1961, alien refugees live in secret on Earth by disguising themselves as humans.',
        )
        self.movie.genre.add(self.genre)
        self.movie.crew.add(self.crew)
        self.role = Role.objects.create(
            name='Officer James Darrel Edwards III, MiB Agent J (Jay)',
            crew=self.crew,
            movie=self.movie,
        )
        self.review = Review.objects.create(
            author=self.user,
            movie=self.movie,
            viewer_rating=(5),
            title='From fresh prince of bel air to fresh prince of our hearts',
            comment='Great movie, great actor.',
            date_posted=datetime(2021,4,9),
        )

    def test_create_crew(self):

        self.assertEqual(self.crew.name, 'Will Smith')
        self.assertEqual(self.crew.birth_date, date(1968, 9, 25))
        self.assertEqual(self.crew.birth_place, 'Philadelphia, Pennsylvania, U.S.')
        self.assertEqual(self.crew.biography, 'Smith was born on September 25, 1968 in Philadelphia, Pennsylvania to Caroline.')

    def test_create_genre(self):

        self.assertEqual(self.genre.genre, 'Sci Fi')

    def test_create_movie(self):

        self.assertEqual(self.movie.title, 'Men in Black')
        self.assertEqual(self.movie.production_company, 'Columbia Pictures, MacDonald Parkes, Amblin Entertainment')
        self.assertEqual(self.movie.distribution_company, 'Sony Pictures Releasing')
        self.assertEqual(self.movie.date_released, date(1997, 4, 2))
        self.assertEqual(self.movie.movie_rated, 'PG-13')
        self.assertEqual(self.movie.movie_length, 98)
        self.assertEqual(self.movie.plot, 'After a government agency makes first contact with aliens in 1961, alien refugees live in secret on Earth by disguising themselves as humans.')
        self.assertEqual(self.movie.genre.first(), self.genre)
        self.assertEqual(self.movie.crew.first(), self.crew)

    def test_create_role(self):

        self.assertEqual(self.role.name, 'Officer James Darrel Edwards III, MiB Agent J (Jay)')
        self.assertEqual(self.role.crew,  self.crew)
        self.assertEqual(self.role.movie, self.movie)

    def test_create_review(self):

        self.assertEqual(self.review.author, self.user)
        self.assertEqual(self.review.movie, self.movie)
        self.assertEqual(self.review.viewer_rating, 5)
        self.assertEqual(self.review.title, 'From fresh prince of bel air to fresh prince of our hearts')
        self.assertEqual(self.review.comment, 'Great movie, great actor.')
        self.assertEqual(self.review.date_posted, datetime(2021,4,9))
