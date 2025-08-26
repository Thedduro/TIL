from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    # 장르 관련
    path('api/v1/genres/', views.GenreListView.as_view(), name='genre-list'),
    
    # 영화 관련
    path('api/v1/movies/', views.MovieListView.as_view(), name='movie-list'),
    path('api/v1/movies/<int:pk>/', views.MovieDetailView.as_view(), name='movie-detail'),
    path('api/v1/movies/<int:movie_pk>/reviews/', views.MovieReviewCreateView.as_view(), name='movie-review-create'),
    
    # 리뷰 관련
    path('api/v1/reviews/', views.ReviewListView.as_view(), name='review-list'),
    path('api/v1/reviews/<str:pk>/', views.ReviewDetailView.as_view(), name='review-detail'),
]
