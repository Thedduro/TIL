# TMDB API 키 설정
API_KEY = '0cf5259798a47c0d99fed1dc25f8c459'
BASE_URL = "https://api.themoviedb.org/3/"

# API 호출 함수
import requests
from pprint import pprint
import csv

# 문제 a에서 생성된 movies.csv 파일을 기반으로 영화 ID 목록 가져오기
with open('movies.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    movie_ids = [row['id'] for row in reader]

credit_results = []
fields = ['cast_id', 'movie_id', 'name', 'character', 'order']

# 영화 캐스팅 정보 수집
for movie_id in movie_ids: # 각 영화들을 하나씩 탐색
    detail_url = f'movie/{movie_id}/credits?api_key={API_KEY}'
    response = requests.get(BASE_URL + detail_url).json()

    # 배우 데이터 처리 함수
    for result in response.get('cast'):
        order = result.get('order')
        if order <=10:  # 상위 10명의 배우만 수집
            # 배우 정보를 temp_item에 저장
            temp_item = {
                'cast_id': result.get('cast_id'),
                'movie_id': movie_id,
                'name': result.get('name'),
                'character': result.get('character'),
                'order': order
            }
            credit_results.append(temp_item)

pprint(credit_results)

# 데이터 수집 및 CSV 파일로 저장
with open('movie_cast.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fields)
    writer.writeheader()
    writer.writerows(credit_results)

