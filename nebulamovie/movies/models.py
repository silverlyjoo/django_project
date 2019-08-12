from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

# title,audience,runtime,grade,popularity,release_date,vote,director,director_id,actorList,overview,images_t,images_h
class Director(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=100)
    audience = models.IntegerField()
    runtime = models.IntegerField()
    grade = models.CharField(max_length=50)
    popularity = models.FloatField()
    release_date = models.DateField()
    vote = models.FloatField()
    actor1 = models.TextField(blank=True)
    actor2 = models.TextField(blank=True)
    actor3 = models.TextField(blank=True)
    overview = models.TextField()
    poster_url_low = models.TextField()
    poster_url = models.TextField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    genres = models.ManyToManyField(Genre, related_name='genre_movies', blank=True)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies', blank=True)
    s_score = models.FloatField(blank=True, null=True)
    p_score = models.FloatField(blank=True, null=True)
    
    def __str__(self):
        return self.title
    
class Score(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    content = models.CharField(max_length=140)
    score = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.content}, ({self.score}점)'
        
class Post(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    content = models.TextField()
    score = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rec_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='rec_posts', blank=True)
    not_rec_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='not_rec_posts', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.title}, {self.content}'