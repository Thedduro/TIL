
# Vue3+Vite 영화/리뷰 SPA 프로젝트 개발 회고

## 1. 프로젝트 세팅 및 구조 설계
- Vite와 Vue3 기반 SPA 프로젝트를 생성하고, vue-router/axios/bootstrap 등 필수 패키지를 설치했다.
- src 폴더 구조를 명확히 분리(api, views, components, router)하여 유지보수성과 확장성을 높였다.
- .env로 TMDB/Youtube API 키를 안전하게 관리하는 방법을 익혔다.

**학습/느낀점:**
- Vite의 빠른 개발 환경과 Vue3의 Composition API 구조에 익숙해질 수 있었다.
- 환경변수(.env) 관리와 gitignore 최신화의 중요성을 체감했다.

## 2. TMDB 영화 목록/상세 구현
- TMDB API를 axios 인스턴스로 래핑해 재사용성과 코드 가독성을 높였다.
- Top Rated 영화 목록을 카드 그리드로, 상세는 2열 레이아웃으로 구현했다.
- 카드 클릭 시 상세 진입, 라우터 props 전달, 로딩/에러/빈 상태 등 UX를 신경썼다.

**어려웠던 점:**
- TMDB API의 인증 방식(v3/v4) 차이와 이미지 URL 처리, 한글 데이터 부족 등에서 시행착오가 있었다.
- 라우터에서 props 전달, 동적 라우팅 등 Vue Router의 다양한 옵션을 실습하며 이해도를 높였다.

## 3. Youtube 예고편/리뷰 연동
- Youtube Data API를 활용해 영화 예고편/리뷰 영상을 검색하고, 모달에서 자동 재생되도록 구현했다.
- 모달 컴포넌트의 상태 관리(visible, videoId 초기화 등)와 iframe autoplay, 닫기 시 재생 중지 등 세부 UX를 신경썼다.
- 검색 결과를 카드 그리드로, 클릭 시 모달 재생 구조로 설계했다.

**새로 배운 것:**
- Vue에서 watch, ref, emit 등 Composition API의 다양한 활용법을 익혔다.
- Youtube API의 쿼리 파라미터, 동적 iframe src, 모달 UX 등 실무적인 연동 경험을 쌓았다.

## 4. UI/UX 개선 및 마무리
- Bootstrap을 활용한 반응형 그리드, 한글 폰트/정렬, 상단 네비게이션 커스텀(로고, 한글 메뉴, 빨간 테두리 등)으로 목표 UI를 구현했다.
- favicon 등 static asset 관리, 컴포넌트 중복(template/script) 에러 해결 등 실제 개발에서 자주 마주치는 문제를 직접 해결했다.

**느낀 점:**
- 실제 API와 연동하며 데이터 흐름, 상태 관리, 컴포넌트 분리의 중요성을 체감했다.
- 에러 메시지(중복 template 등)와 해결 과정에서 Vue SFC 구조에 대한 이해가 깊어졌다.
- 요구사항을 단계별로 쪼개어 구현하고, 각 단계마다 테스트/리팩토링하는 습관이 중요함을 느꼈다.

---
이 프로젝트를 통해 Vue3 SPA 개발의 전 과정을 실습하며, 실무에서 필요한 API 연동, 상태 관리, UI/UX 구현, 에러 디버깅 등 다양한 경험을 쌓을 수 있었다.
