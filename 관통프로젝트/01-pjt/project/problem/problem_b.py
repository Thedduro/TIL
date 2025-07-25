# TMDB API 키 설정
API_KEY = '0cf5259798a47c0d99fed1dc25f8c459'
BASE_URL = "https://api.themoviedb.org/3/"

# API 호출 함수
import requests
from pprint import pprint
import csv

# 영화 상세 데이터 처리 함수

# CSV 파일에서 영화 ID 읽기
with open('movies.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    movie_ids = [row['id'] for row in reader]

results = []
fields = ['id', 'budget', 'revenue', 'runtime', 'genres']

# 영화 상세 데이터 수집
for movie_id in movie_ids: 
    detail_url = f'movie/{movie_id}?api_key={API_KEY}'
    response = requests.get(BASE_URL + detail_url).json()

    # 각 영화의 상세 정보를 추출하여 results 리스트에 추가
    temp_item = {}
    for key in fields:
        if key == 'genres':
            temp_item[key] = ', '.join([genre['name'] for genre in response['genres']])
        else:
            temp_item[key]= response[key]
    results.append(temp_item)

# 데이터 수집 및 CSV 파일로 저장
with open('movie_details.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fields)
    writer.writeheader()
    writer.writerows(results)