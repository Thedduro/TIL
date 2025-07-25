# TMDB API 키 설정
API_KEY = '0cf5259798a47c0d99fed1dc25f8c459'
BASE_URL = "https://api.themoviedb.org/3/"

# API 호출 함수
import requests
from pprint import pprint
import csv

# movie 정보를 로드하는 함수 (problem_a.py의 결과 활용)
# 문제 a에서 생성된 movies.csv 파일을 기반으로 영화 ID 목록 가져오기
with open('movies.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    movie_ids = [row['id'] for row in reader]


movie_rating_dic = {}   
# F03에서 수집한 평점 데이터 처리 함수(각 영화별)
with open('movie_reviews.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        movie_id = row['movie_id']
        rating = str(int(float(row['rating'])))

        # movie_id별 딕셔너리가 없으면 생성
        if movie_id not in movie_rating_dic:
            movie_rating_dic[movie_id] = {}

        # 해당 평점에 대한 카운트 증가
        if rating not in movie_rating_dic[movie_id]:
            movie_rating_dic[movie_id][rating] = 1
        else:
            movie_rating_dic[movie_id][rating] += 1

fields = ['movie_id', 'average_rating', 'vote_count', 'rating_distribution']
vote_results = []

# 각 영화들을 하나씩 탐색
for movie_id in movie_ids:
    detail_url = f'movie/{movie_id}?api_key={API_KEY}'
    response = requests.get(BASE_URL + detail_url).json()
    
    temp_item = {
        'movie_id' : movie_id,
        'average_rating' : response.get('vote_average'),
        'vote_count' : response.get('vote_count')
        }
    
    # 영화 아이디를 매핑해서 점수 분포 딕셔너리를 temp_dic에 추가한다
    if movie_id in movie_rating_dic.keys():
        temp_item['rating_distribution'] = movie_rating_dic[movie_id]
    
    vote_results.append(temp_item)

# 데이터 수집 및 CSV 파일로 저장
with open('movie_ratings.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fields)
    writer.writeheader()
    writer.writerows(vote_results)