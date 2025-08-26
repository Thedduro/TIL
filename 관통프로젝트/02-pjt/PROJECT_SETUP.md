# 02-pjt: DB 설계를 활용한 REST API 서버 구축

## 프로젝트 개요

Django REST framework(DRF)를 사용하여 영화 정보 및 리뷰 커뮤니티를 위한 백엔드 API 서버를 개발한 프로젝트입니다.

## 주요 기술

- **Python 3.11+**
- **Django 5.2.x**
- **Django REST framework 3.14.0**
- **MySQL 8.0** (데이터베이스)
- **dj-rest-auth 5.0.2**
- **django-allauth 0.60.1**

## 프로젝트 구조

```
02-pjt/
├── config/                 # Django 프로젝트 설정
├── movies/                 # 영화 앱
│   ├── models.py          # 데이터베이스 모델
│   ├── serializers.py     # API 시리얼라이저
│   ├── views.py           # API 뷰
│   ├── urls.py            # URL 패턴
│   └── management/        # 데이터 로드 명령어
├── accounts/              # 사용자 인증 앱
│   ├── views.py           # 인증 뷰
│   └── urls.py            # 인증 URL 패턴
├── problem/               # 원본 데이터
│   └── data/              # CSV 데이터 파일들
├── docker-compose.yml     # MySQL Docker 설정
├── requirements.txt       # 프로젝트 의존성
└── MYSQL_SETUP.md         # MySQL 설정 가이드
```

## 데이터베이스 모델

### Genre (장르)
- `id`: 기본 키
- `name`: 장르 이름

### Movie (영화)
- `id`: 영화 ID (기본 키)
- `title`: 영화 제목
- `release_date`: 개봉일
- `popularity`: 인기도
- `budget`: 제작비
- `revenue`: 수익
- `runtime`: 상영시간
- `genres`: 장르 (M:N 관계)

### Cast (출연진)
- `id`: 출연진 ID (기본 키)
- `name`: 배우 이름
- `character`: 배역명
- `order`: 출연 순서
- `movie`: 영화 (1:N 관계)

### Review (리뷰)
- `id`: 리뷰 ID (기본 키)
- `author`: 작성자 (User 모델 참조)
- `content`: 리뷰 내용
- `rating`: 평점
- `movie`: 영화 (1:N 관계)
- `created_at`: 작성일
- `updated_at`: 수정일

## API 엔드포인트

### 인증 관련
- `POST /accounts/signup/` - 회원가입
- `POST /accounts/login/` - 로그인

### 장르 관련
- `GET /api/v1/genres/` - 전체 장르 목록 조회 (F02)

### 영화 관련
- `GET /api/v1/movies/` - 전체 영화 목록 조회 (F03)
- `GET /api/v1/movies/<movie_pk>/` - 단일 영화 상세 정보 조회 (F04)
- `POST /api/v1/movies/<movie_pk>/reviews/` - 특정 영화에 대한 리뷰 생성 (F07)

### 리뷰 관련
- `GET /api/v1/reviews/` - 전체 리뷰 목록 조회 (F05)
- `GET /api/v1/reviews/<review_pk>/` - 단일 리뷰 조회 (F06)
- `PUT /api/v1/reviews/<review_pk>/` - 리뷰 전체 수정 (F06)
- `PATCH /api/v1/reviews/<review_pk>/` - 리뷰 부분 수정 (F06)
- `DELETE /api/v1/reviews/<review_pk>/` - 리뷰 삭제 (F06)

## 구현된 기능

### 1단계: 프로젝트 설정 및 데이터베이스 구축 (F01)
- ✅ Django 프로젝트 및 앱 생성
- ✅ 모델 정의 (Genre, Movie, Cast, Review)
- ✅ MySQL 데이터베이스 연동
- ✅ 데이터베이스 마이그레이션
- ✅ CSV 데이터 파싱 및 DB 삽입

### 2단계: 필수 API 엔드포인트 구현
- ✅ 전체 장르 목록 조회 (F02)
- ✅ 전체 영화 목록 조회 (F03)
- ✅ 단일 영화 상세 정보 조회 (F04)
- ✅ 전체 리뷰 목록 조회 (F05)
- ✅ 단일 리뷰 조회, 수정, 삭제 (F06)
- ✅ 특정 영화에 대한 리뷰 생성 (F07)

### 3단계: 도전 과제 구현
- ✅ 인증 및 권한 기능 구현 (F08)
  - dj-rest-auth 설치 및 설정
  - accounts 앱 생성
  - 회원가입/로그인 엔드포인트 구현
  - Review 모델의 author 필드를 User 모델 참조로 변경
  - 인증된 사용자만 API 접근 가능하도록 권한 설정
  - 리뷰 수정/삭제는 작성자만 가능하도록 권한 제한
- ✅ 영화 평점 통계 정보 추가 (F09)
  - 단일 영화 상세 정보에 평균 평점과 총 투표 수 추가
  - SerializerMethodField 사용
  - Django ORM의 Avg와 Count 집계 함수 활용

## 설치 및 실행 방법

### 1. 의존성 설치
```bash
pip install -r requirements.txt
```

### 2. MySQL 설정
자세한 MySQL 설정 방법은 [MYSQL_SETUP.md](MYSQL_SETUP.md)를 참조하세요.

#### Docker 사용 (권장)
```bash
docker-compose up -d
```

#### 또는 XAMPP/MySQL 직접 설치
- MySQL 서버 실행
- `movie_db` 데이터베이스 생성

### 3. 데이터베이스 마이그레이션
```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. 초기 데이터 로드
```bash
python manage.py load_data
```

### 5. 개발 서버 실행
```bash
python manage.py runserver
```

## 학습 내용

### Django REST Framework
- **Generic Views**: ListAPIView, RetrieveAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView 활용
- **Serializers**: ModelSerializer, SerializerMethodField를 사용한 데이터 직렬화
- **Permissions**: IsAuthenticated, IsAuthenticatedOrReadOnly를 통한 권한 관리
- **URL Patterns**: RESTful API 설계 원칙에 따른 URL 구조

### 데이터베이스 설계
- **관계 설정**: ForeignKey(1:N), ManyToManyField(M:N) 활용
- **집계 함수**: Avg, Count를 사용한 통계 데이터 계산
- **마이그레이션**: 모델 변경사항 관리
- **MySQL 연동**: Django와 MySQL 데이터베이스 연동

### 인증 및 권한
- **dj-rest-auth**: REST API 인증 라이브러리 활용
- **사용자 권한**: 리뷰 작성자만 수정/삭제 가능하도록 제한
- **세션 인증**: SessionAuthentication 사용

### 데이터 처리
- **CSV 파싱**: Python csv 모듈을 사용한 데이터 파싱
- **관리 명령어**: Django management command를 통한 데이터 로드
- **데이터 검증**: 입력 데이터 유효성 검사 및 오류 처리

## API 테스트

Postman을 사용하여 모든 엔드포인트를 테스트할 수 있습니다:

1. **회원가입**: `POST /accounts/signup/`
   ```json
   {
     "username": "testuser",
     "password": "testpass123",
     "email": "test@example.com"
   }
   ```

2. **로그인**: `POST /accounts/login/`
   ```json
   {
     "username": "testuser",
     "password": "testpass123"
   }
   ```

3. **영화 목록 조회**: `GET /api/v1/movies/`

4. **영화 상세 조회**: `GET /api/v1/movies/<movie_id>/`

5. **리뷰 생성**: `POST /api/v1/movies/<movie_id>/reviews/`
   ```json
   {
     "content": "정말 좋은 영화입니다!",
     "rating": 4.5
   }
   ```

## 개발자

- **개발일자**: 2025년 8월 22일
- **프로젝트명**: 02-pjt: DB 설계를 활용한 REST API 서버 구축
- **데이터베이스**: MySQL 8.0
