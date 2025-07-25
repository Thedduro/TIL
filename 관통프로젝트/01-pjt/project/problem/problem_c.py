# TMDB API 키 설정
API_KEY = '0cf5259798a47c0d99fed1dc25f8c459'
BASE_URL = "https://api.themoviedb.org/3/"

# API 호출 함수
import requests
from pprint import pprint
import csv

# 영화 ID 리스트를 movies.csv 파일에서 읽어옴
with open('movies.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    movie_ids = [row['id'] for row in reader]

reviews_results = []
fields = ['review_id', 'movie_id', 'author', 'content', 'rating']

# 영화 리뷰 아이디 수집
for movie_id in movie_ids: 
    detail_url = f'movie/{movie_id}/reviews?api_key={API_KEY}'
    response = requests.get(BASE_URL + detail_url).json()

    # 각 영화의 리뷰 정보를 추출하여 reviews_results 리스트에 추가
    for result in response.get('results'):
        rating = result.get('author_details').get('rating')

        if rating is not None and rating >= 5: # 평점이 5 이상인 리뷰만 수집
            # 리뷰 정보를 temp_item에 저장
            temp_item = {
                'review_id': result.get('id'),
                'movie_id': movie_id,
                'author': result.get('author'),
                'content': result.get('content') if result.get('content') else '내용 없음',
                'rating' : rating
            }

            reviews_results.append(temp_item)

# 데이터 수집 및 CSV 파일로 저장
with open('movie_reviews.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fields)
    writer.writeheader()
    writer.writerows(reviews_results)
