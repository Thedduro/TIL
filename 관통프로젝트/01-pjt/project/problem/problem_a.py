# TMDB API 키 설정
API_KEY = '0cf5259798a47c0d99fed1dc25f8c459'
BASE_URL = "https://api.themoviedb.org/3/"

# API 호출 함수
import requests
from pprint import pprint
import csv

detail_url = "movie/popular?api_key=" + API_KEY + "&language=en-US&page=1"
response = requests.get(BASE_URL+detail_url).json()

# 영화 데이터 처리 함수

# 데이터 수집 및 CSV 파일로 저장
result = []

fields  = ['id', 'title', 'release_date', 'popularity']

for item in response['results']:
    temp_item = {}

    for key in fields:
        temp_item[key]= item[key]

    result.append(temp_item)
pprint(result)

with open('movies.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fields)
    writer.writeheader()
    writer.writerows(result)

pprint(response)