from django.db import models
from django.contrib.auth.models import User

class Genre(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Movie(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    release_date = models.DateField()
    popularity = models.FloatField()
    budget = models.BigIntegerField(default=0)
    revenue = models.BigIntegerField(default=0)
    runtime = models.IntegerField(null=True, blank=True)
    genres = models.ManyToManyField(Genre, related_name='movies')
    
    def __str__(self):
        return self.title

class Cast(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    character = models.CharField(max_length=200)
    order = models.IntegerField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='cast_set')
    
    def __str__(self):
        return f"{self.name} as {self.character}"
    
    class Meta:
        ordering = ['order']

class Review(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    content = models.TextField()
    rating = models.FloatField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='review_set')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.author.username}'s review of {self.movie.title}"
