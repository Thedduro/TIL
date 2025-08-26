# 영화 리뷰 API 서버 구축 프로젝트

## 1. 프로젝트 개요

**Django REST Framework(DRF)**를 활용하여 영화 리뷰 데이터를 관리하는 API 서버를 구축하는 프로젝트입니다. 사용자 인증(회원가입, 로그인) 기능을 구현하고, 인증된 사용자가 영화 리뷰를 생성(Create), 조회(Read), 수정(Update), 삭제(Delete)할 수 있는 CRUD API를 개발했습니다.

---

## 2. 주요 기능 및 API Endpoints

| 기능 | HTTP Method | URL Endpoint | 설명 |
| --- | --- | --- | --- |
| **회원가입** | `POST` | `/accounts/signup/` | 새로운 사용자를 생성합니다. |
| **로그인** | `POST` | `/accounts/login/` | 사용자 인증 후 **인증 토큰(Token)**을 발급합니다. |
| **리뷰 목록 조회** | `GET` | `/reviews/` | 전체 리뷰 목록을 조회합니다. |
| **리뷰 상세 조회** | `GET` | `/reviews/<int:review_id>/` | 특정 ID의 리뷰를 상세 조회합니다. |
| **리뷰 작성** | `POST` | `/reviews/` | 새로운 리뷰를 작성합니다. (로그인 필요) |
| **리뷰 수정** | `PUT` / `PATCH` | `/reviews/<int:review_id>/` | 특정 리뷰를 수정합니다. (작성자 본인만 가능) |
| **리뷰 삭제** | `DELETE` | `/reviews/<int:review_id>/` | 특정 리뷰를 삭제합니다. (작성자 본인만 가능) |

---

## 3. 주요 트러블슈팅 및 학습 내용

### 가. 인증 (Authentication) 문제 해결

#### 문제 상황: `403 Forbidden` 에러의 연속
-   `GET` 요청은 성공하지만, 데이터를 변경하는 `POST`, `PUT`, `DELETE` 요청 시 계속해서 `403 Forbidden` 에러가 발생했습니다.
-   로그인(`POST /accounts/login/`) 요청 시 `200 OK`는 뜨지만, 응답 Body에 `access token`이나 `sessionid` 쿠키가 없어 인증 상태를 유지할 수 없었습니다.

#### 원인 분석 및 해결 과정
1.  **CSRF 토큰 누락**: DRF의 보안 정책상 데이터 변경 요청에는 `X-CSRFToken` 헤더가 필요하다는 것을 알게 되었습니다. 하지만 Postman에서 이 헤더를 추가해도 문제가 해결되지 않았습니다.
2.  **`authenticate`와 `login` 함수의 차이**: 로그인 로직을 확인한 결과, `authenticate` 함수로 사용자 정보가 유효한지 **확인**만 하고, 실제 로그인 상태를 만들어주는 `login` 함수나 토큰을 생성하는 로직이 누락된 것을 발견했습니다.
3.  **토큰 기반 인증 구현**: `rest_framework.authtoken`을 사용하여, 로그인 성공 시 해당 사용자의 토큰을 생성하고 응답 Body에 포함시켜주는 로직을 `LoginView`에 추가하여 문제를 해결했습니다.

```python
# views.py - LoginView 수정 후
from rest_framework.authtoken.models import Token

# ...
user = authenticate(username=username, password=password)
if user:
    token, created = Token.objects.get_or_create(user=user)
    return Response({'token': token.key}) # 응답에 토큰 추가
```

### 나. 데이터베이스 모델링 및 설정

#### 어려웠던 부분
-   **모델 관계 설정**: 초기 설계 단계에서 영화와 배우, 장르 간의 M:N(다대다) 관계와 사용자와 리뷰 간의 1:N(일대다) 관계를 올바르게 설정하는 것이 어려웠습니다.
-   **필드 타입 선택**: `budget`, `revenue` 같이 매우 큰 숫자를 저장해야 하는 필드에 일반 `IntegerField`를 사용하려 했으나, 값의 범위를 초과할 수 있다는 것을 깨닫고 `BigIntegerField`를 사용해야 함을 알게 되었습니다.

#### 새로 배운 것
-   `ManyToManyField`와 `ForeignKey`를 사용한 모델 관계 설정 방법
-   `BigIntegerField`의 존재와 올바른 용도
-   모델 필드 옵션인 `null=True`와 `blank=True`의 정확한 차이점

### 다. 데이터베이스 연동 및 마이그레이션

-   Django 프로젝트와 로컬 MySQL 데이터베이스를 연동하는 방법을 학습했습니다. `settings.py` 파일에 데이터베이스 접속 정보를 설정하고, `mysqlclient` 라이브러리를 설치하여 연동을 완료했습니다.
-   `makemigrations`와 `migrate` 명령어를 통해 Django 모델의 변경사항을 데이터베이스 스키마에 안전하게 적용하는 마이그레이션 시스템의 중요성을 이해했습니다.

```python
# settings.py 예시
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'movie_pjt_db',
        # ...
    }
}
```

---

## 4. 프로젝트 후기 (느낀 점)

-   **API 동작 원리 이해**: Postman을 통해 직접 HTTP 요청을 보내고 응답을 분석하면서, `GET`, `POST`, `PUT` 등 각 메소드의 역할과 인증 토큰이 어떻게 동작하는지 명확하게 이해할 수 있었습니다.
-   **에러 메시지의 중요성**: `403 Forbidden`, `401 Unauthorized`, `404 Not Found` 등 다양한 HTTP 상태 코드가 각각 어떤 의미를 가지는지, 그리고 에러 발생 시 터미널에 출력되는 Django의 상세한 로그(Traceback)를 읽고 디버깅하는 능력이 향상되었습니다.
-   **문서의 소중함**: 문제가 발생했을 때, 공식 문서(Django, DRF)를 참고하는 것이 가장 정확하고 빠른 해결책이라는 것을 다시 한번 깨달았습니다.
