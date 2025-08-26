# MySQL 설정 가이드

## 🚀 MySQL 설치 및 설정 방법

### 방법 1: Docker 사용 (권장)

1. **Docker 설치**
   - [Docker Desktop](https://www.docker.com/products/docker-desktop/) 설치

2. **MySQL 컨테이너 실행**
   ```bash
   docker-compose up -d
   ```

3. **MySQL 상태 확인**
   ```bash
   docker ps
   ```

### 방법 2: XAMPP 설치

1. **XAMPP 다운로드 및 설치**
   - [XAMPP 다운로드](https://www.apachefriends.org/)
   - 설치 후 MySQL 서비스 시작

2. **MySQL 설정**
   - 기본 사용자: `root`
   - 기본 비밀번호: `(없음)`
   - 포트: `3306`

### 방법 3: MySQL Community Server

1. **MySQL Community Server 설치**
   - [MySQL 다운로드](https://dev.mysql.com/downloads/mysql/)
   - 설치 시 root 비밀번호 설정

## 🔧 Django 설정

### 1. 데이터베이스 생성

MySQL에 접속하여 데이터베이스를 생성합니다:

```sql
CREATE DATABASE movie_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

### 2. Django 마이그레이션

```bash
python manage.py makemigrations
python manage.py migrate
```

### 3. 초기 데이터 로드

```bash
python manage.py load_data
```

## 📋 데이터베이스 설정 확인

### 현재 설정 (config/settings.py)
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'movie_db',
        'USER': 'root',
        'PASSWORD': '1234',
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            'charset': 'utf8mb4',
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}
```

### 설정 변경이 필요한 경우

1. **XAMPP 사용 시**:
   ```python
   'PASSWORD': '',  # 비밀번호 없음
   ```

2. **다른 사용자 사용 시**:
   ```python
   'USER': 'your_username',
   'PASSWORD': 'your_password',
   ```

## 🐛 문제 해결

### 1. MySQL 연결 오류
```
Error: 1045 (28000): Access denied for user 'root'@'localhost'
```
**해결 방법**:
- 비밀번호 확인
- MySQL 서비스 실행 상태 확인
- 사용자 권한 확인

### 2. 데이터베이스 없음 오류
```
Error: 1049 (42000): Unknown database 'movie_db'
```
**해결 방법**:
```sql
CREATE DATABASE movie_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

### 3. 문자셋 오류
```
Error: 1366 (HY000): Incorrect string value
```
**해결 방법**:
- utf8mb4 문자셋 사용 확인
- 데이터베이스 생성 시 CHARACTER SET 지정

## ✅ 확인 사항

1. **MySQL 서비스 실행 중**
2. **데이터베이스 생성 완료**
3. **Django 설정 파일 수정**
4. **마이그레이션 완료**
5. **초기 데이터 로드 완료**

## 🎯 최종 테스트

```bash
python manage.py runserver
```

브라우저에서 `http://localhost:8000/api/v1/movies/` 접속하여 API 동작 확인


