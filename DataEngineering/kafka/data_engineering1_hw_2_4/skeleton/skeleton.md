# Python으로 작성한 로그 모니터링 스크립트를 도커 컨테이너에서 실행하고, 볼륨 마운트를 통해 실시간 로그 파일을 읽는 구조를 구성

# Step 1: 실습 디렉토리 생성 및 이동
mkdir log-watcher
cd log-watcher

# Step 2: 로그 파일 생성 (호스트에서 실시간으로 쓰일 파일)
echo "Initial log line" > app.log

# Step 3: 로그 모니터링 스크립트 작성
# watch_log.py 파일을 적절한 위치에 위치시켜주세요.

# Step 4: Dockerfile 작성
# Dockerfile을 적절한 위치에 위치시켜주세요.


# Step 5: Docker 이미지 빌드
docker build -t __________ .

# Step 6: 도커 컨테이너 실행 (볼륨 마운트로 호스트의 로그 파일 연결)
docker run -v $(pwd)/app.log:/log/app.log ____________


# Step 7: 테스트용 로그 추가
# (다른 터미널에서 실행) → 컨테이너 콘솔에 출력되는지 확인
echo "New log entry" >> app.log


![alt text](image.png)