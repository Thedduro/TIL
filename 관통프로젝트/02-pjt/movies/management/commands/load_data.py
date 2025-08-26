import csv
import os
from datetime import datetime
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from movies.models import Genre, Movie, Cast, Review

class Command(BaseCommand):
    help = 'Load movie data from CSV files'

    def handle(self, *args, **options):
        # 데이터 파일 경로
        base_path = 'problem/data'
        
        # 1. 장르 데이터 로드
        self.stdout.write('Loading genres...')
        genres_dict = {}
        
        # movies.csv에서 장르 정보 추출
        movies_csv_path = os.path.join(base_path, 'movies.csv')
        movie_details_csv_path = os.path.join(base_path, 'movie_details.csv')
        
        with open(movie_details_csv_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['genres']:
                    genre_names = [name.strip() for name in row['genres'].split(',')]
                    for genre_name in genre_names:
                        if genre_name not in genres_dict:
                            genre, created = Genre.objects.get_or_create(name=genre_name)
                            genres_dict[genre_name] = genre
        
        self.stdout.write(f'Loaded {len(genres_dict)} genres')
        
        # 2. 영화 데이터 로드
        self.stdout.write('Loading movies...')
        movies_dict = {}
        
        # movies.csv 읽기
        with open(movies_csv_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                movie_id = int(row['id'])
                release_date = datetime.strptime(row['release_date'], '%Y-%m-%d').date()
                
                movie = Movie.objects.create(
                    id=movie_id,
                    title=row['title'],
                    release_date=release_date,
                    popularity=float(row['popularity'])
                )
                movies_dict[movie_id] = movie
        
        # movie_details.csv에서 추가 정보 업데이트
        with open(movie_details_csv_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                movie_id = int(row['movie_id'])
                if movie_id in movies_dict:
                    movie = movies_dict[movie_id]
                    movie.budget = int(row['budget']) if row['budget'] and row['budget'] != '0' else 0
                    movie.revenue = int(row['revenue']) if row['revenue'] and row['revenue'] != '0' else 0
                    movie.runtime = int(row['runtime']) if row['runtime'] and row['runtime'] != '0' else None
                    movie.save()
                    
                    # 장르 연결
                    if row['genres']:
                        genre_names = [name.strip() for name in row['genres'].split(',')]
                        for genre_name in genre_names:
                            if genre_name in genres_dict:
                                movie.genres.add(genres_dict[genre_name])
        
        self.stdout.write(f'Loaded {len(movies_dict)} movies')
        
        # 3. 출연진 데이터 로드
        self.stdout.write('Loading cast...')
        cast_csv_path = os.path.join(base_path, 'movie_cast.csv')
        
        with open(cast_csv_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                movie_id = int(row['movie_id'])
                if movie_id in movies_dict:
                    Cast.objects.create(
                        id=int(row['cast_id']),
                        name=row['name'],
                        character=row['character'],
                        order=int(row['order']),
                        movie=movies_dict[movie_id]
                    )
        
        self.stdout.write('Loaded cast data')
        
        # 4. 리뷰 데이터 로드
        self.stdout.write('Loading reviews...')
        reviews_csv_path = os.path.join(base_path, 'movie_reviews.csv')
        
        # 기본 사용자 생성 (리뷰 작성자용)
        default_user, created = User.objects.get_or_create(
            username='anonymous',
            defaults={'email': 'anonymous@example.com'}
        )
        
        with open(reviews_csv_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                movie_id = int(row['movie_id'])
                if movie_id in movies_dict:
                    Review.objects.create(
                        id=row['review_id'],
                        author=default_user,
                        content=row['content'],
                        rating=float(row['rating']),
                        movie=movies_dict[movie_id]
                    )
        
        self.stdout.write('Loaded review data')
        self.stdout.write(self.style.SUCCESS('Successfully loaded all data'))
