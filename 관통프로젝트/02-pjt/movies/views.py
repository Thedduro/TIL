from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from django.shortcuts import get_object_or_404
from .models import Genre, Movie, Review
from .serializers import (
    GenreSerializer, MovieListSerializer, MovieDetailSerializer,
    ReviewListSerializer, ReviewDetailSerializer, ReviewCreateSerializer
)

class GenreListView(generics.ListAPIView):
    """전체 장르 목록 조회 (F02)"""
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class MovieListView(generics.ListAPIView):
    """전체 영화 목록 조회 (F03)"""
    queryset = Movie.objects.all()
    serializer_class = MovieListSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class MovieDetailView(generics.RetrieveAPIView):
    """단일 영화 상세 정보 조회 (F04)"""
    queryset = Movie.objects.all()
    serializer_class = MovieDetailSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class ReviewListView(generics.ListAPIView):
    """전체 리뷰 목록 조회 (F05)"""
    queryset = Review.objects.all()
    serializer_class = ReviewListSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    """단일 리뷰 조회, 수정, 삭제 (F06)"""
    queryset = Review.objects.all()
    serializer_class = ReviewDetailSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get_permissions(self):
        # 모든 요청에 대해 AllowAny 권한 사용 (임시)
        from rest_framework.permissions import AllowAny
        return [AllowAny()]
    
    def update(self, request, *args, **kwargs):
        # 임시로 권한 검사 비활성화
        return super().update(request, *args, **kwargs)
    
    def destroy(self, request, *args, **kwargs):
        # 임시로 권한 검사 비활성화
        return super().destroy(request, *args, **kwargs)

class MovieReviewCreateView(generics.CreateAPIView):
    """특정 영화에 대한 리뷰 생성 (F07)"""
    serializer_class = ReviewCreateSerializer
    permission_classes = []  # 모든 권한 제거
    
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['movie_pk'] = self.kwargs['movie_pk']
        return context
