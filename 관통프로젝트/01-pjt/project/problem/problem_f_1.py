# TMDB API 키 설정
API_KEY = '0cf5259798a47c0d99fed1dc25f8c459'
BASE_URL = "https://api.themoviedb.org/3/"

# API 호출 함수
import requests
from pprint import pprint
import csv

# movie 정보를 로드하는 함수 (problem_a.py의 결과 활용)
# 문제 a에서 생성된 movies.csv 파일을 기반으로 영화 ID 목록 가져오기
with open('movie_details.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    rate_revenue = []
    for row in reader:
        #0 이 아닌때만, 계산
        revenue = float(row['revenue'])
        budget = float(row['budget'])
        if revenue !=0 and budget != 0:
            rate_revenue.append([row['id'], revenue/budget])

# 수익률 기준 정렬 > 맨 앞에 id를 찾아냄
sorted_data_high_id = sorted(rate_revenue, key=lambda x: x[1], reverse=True)[0][0]

with open('movies.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        if sorted_data_high_id in row['id']:
            print(row)