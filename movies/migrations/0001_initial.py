# Generated by Django 3.2 on 2021-04-12 19:54

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('genre', models.CharField(max_length=200, unique=True, verbose_name='Genre')),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('production_company', models.CharField(blank=True, max_length=200, verbose_name='Production Company')),
                ('distribution_company', models.CharField(blank=True, max_length=200, verbose_name='Distributed By')),
                ('date_released', models.DateField(blank=True, default=None, null=True, verbose_name='Release Date')),
                ('movie_rated', models.CharField(blank=True, max_length=5, verbose_name='Rated')),
                ('movie_length', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(51420)], verbose_name='Running Time')),
                ('plot', models.TextField(blank=True, max_length=5000, verbose_name='Plot')),
                ('genre', models.ManyToManyField(blank=True, related_name='movies', to='movies.Genre', verbose_name='Genre')),
            ],
        ),
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='Birthday')),
                ('birth_place', models.CharField(blank=True, max_length=200, verbose_name='Birthplace')),
                ('biography', models.TextField(blank=True, max_length=5000, verbose_name='Bio')),
            ],
            options={
                'verbose_name_plural': 'People',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('viewer_rating', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)], verbose_name='Viewer Rating')),
                ('title', models.CharField(blank=True, max_length=60)),
                ('comment', models.TextField(blank=True, max_length=300)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to=settings.AUTH_USER_MODEL, verbose_name='User')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='movies.movie', verbose_name='Movie')),
            ],
        ),
        migrations.CreateModel(
            name='CastAndCrew',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=200, verbose_name='Role')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='roles', to='movies.movie')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='roles', to='movies.people')),
            ],
            options={
                'verbose_name': 'Cast and Crew',
                'verbose_name_plural': 'Cast and Crew',
            },
        ),
    ]
