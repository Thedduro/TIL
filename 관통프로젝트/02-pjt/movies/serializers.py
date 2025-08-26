from rest_framework import serializers
from django.db.models import Avg, Count
from .models import Genre, Movie, Cast, Review
from django.contrib.auth.models import User

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name']

class CastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cast
        fields = ['id', 'name', 'character', 'order']

class MovieListSerializer(serializers.ModelSerializer):
    genres = serializers.SerializerMethodField()
    
    class Meta:
        model = Movie
        fields = ['id', 'title', 'release_date', 'popularity', 'budget', 'revenue', 'runtime', 'genres']
    
    def get_genres(self, obj):
        return [genre.id for genre in obj.genres.all()]

class MovieDetailSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True, read_only=True)
    cast_set = CastSerializer(many=True, read_only=True)
    review_set = serializers.SerializerMethodField()
    average_rating = serializers.SerializerMethodField()
    vote_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Movie
        fields = ['id', 'title', 'release_date', 'popularity', 'budget', 'revenue', 'runtime', 
                 'genres', 'cast_set', 'review_set', 'average_rating', 'vote_count']
    
    def get_review_set(self, obj):
        reviews = obj.review_set.all()
        return [{'id': review.id, 'author': review.author.username, 'content': review.content, 'rating': review.rating} for review in reviews]
    
    def get_average_rating(self, obj):
        avg_rating = obj.review_set.aggregate(Avg('rating'))['rating__avg']
        return round(avg_rating, 2) if avg_rating else 0.0
    
    def get_vote_count(self, obj):
        return obj.review_set.count()

class ReviewListSerializer(serializers.ModelSerializer):
    movie = serializers.SerializerMethodField()
    
    class Meta:
        model = Review
        fields = ['id', 'author', 'content', 'rating', 'movie']
    
    def get_movie(self, obj):
        return {'id': obj.movie.id, 'title': obj.movie.title}

class ReviewDetailSerializer(serializers.ModelSerializer):
    movie = serializers.SerializerMethodField()
    
    class Meta:
        model = Review
        fields = ['id', 'author', 'content', 'rating', 'movie', 'created_at', 'updated_at']
        read_only_fields = ['id', 'author', 'movie', 'created_at', 'updated_at']
    
    def get_movie(self, obj):
        return {'id': obj.movie.id, 'title': obj.movie.title}

class ReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['content', 'rating']
    
    def create(self, validated_data):
        movie_pk = self.context['movie_pk']
        # 임시로 anonymous 사용자 사용
        user = User.objects.get(username='anonymous')
        review_id = f"review_{movie_pk}_{user.id}_{Review.objects.count() + 1}"
        
        return Review.objects.create(
            id=review_id,
            movie_id=movie_pk,
            author=user,
            **validated_data
        )
