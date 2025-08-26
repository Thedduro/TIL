import csv
import requests

# 파일 경로 설정
input_file_path = 'users.csv'
api_url = 'http://127.0.0.1:8000/accounts/signup/'  # Django 서버의 회원 가입 엔드포인트

# 입력 파일 읽고 데이터 변환
def read_and_prepare_user_data(file_path):
    users = {}
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            user_id = row['id']
            if user_id not in users:
                users[user_id] = {
                    'username': row['username'],
                    'first_name': row['first_name'],
                    'last_name': row['last_name'],
                    'email': row['email'],
                    'password1': 'defaultpassword123',
                    'password2': 'defaultpassword123'
                }
    return list(users.values())

# 사용자 데이터로 회원 가입 API 호출
def register_users(users, api_url):
    # 모든 유저 정보를 토대로 회원가입 요청
    for user in users:
        response = requests.post(api_url, data=user)
        if response.status_code == 201:
            print('성공적으로 회원가입 완료!')
        else:
            print('모종의 이유로 회원가입 실패!')
        

users = read_and_prepare_user_data(input_file_path)
register_users(users, api_url)
