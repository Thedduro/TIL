# 실제 Python 기반의 Flask 웹 애플리케이션을 Docker 컨테이너로 배포

# Step 1: 실습 디렉토리 생성 및 이동
# - Flask 앱과 관련 파일들을 저장할 작업 폴더를 생성하고 이동합니다.
mkdir _________
cd _________

# Step 2: Flask 앱 파일(app.py) 생성
# - Python으로 Flask 웹 서버를 구성합니다.
# 디렉토리에 파일을 잘 위치시켜 주세요.

# Step 3: requirements.txt 작성
# - Flask 실행에 필요한 패키지를 나열합니다.
# - 최소한 'flask' 한 줄만 포함되면 됩니다.
echo "________" > requirements.txt

# Step 4: Dockerfile 작성
# - Flask 앱을 실행하기 위한 컨테이너 환경을 정의합니다.
# 디렉토리에 파일을 잘 위치시켜주세요.


# Step 5: Docker 이미지 빌드
# - 현재 디렉토리에 있는 Dockerfile을 기반으로 도커 이미지를 생성합니다.
# - 이미지 이름은 자유롭게 지정 가능합니다 (예: flask-docker-app)
docker build -t ____________ .

# Step 6: 컨테이너 실행
# - 빌드한 이미지를 사용해 컨테이너를 실행하고,
# - 외부의 5000번 포트를 컨테이너의 5000번 포트와 연결합니다.
# - 컨테이너 이름도 지정해야 합니다 (예: flask-container)
docker run -d -p 5000:5000 --name _________ ____________

![alt text](image.png)