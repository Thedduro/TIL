import sys
sys.stdin = open('input.txt')

'''사고 전환
    1. 어차피 사과는 순서대로 먹는데다가
    2. bfs 탐색이면 제일 먼저 도착한 후보가 무조건 가장 효율적이다.
    3. 그럼, 1번 사과 제일 빨리 먹은 경우, 2번 사과 제일빨리 먹은 경우 나누면되는거아님?
    4. 사과 좌표 찾아서 그것대로 처리하자.
'''


from collections import deque

# 우회전만 가능?
# 우 하 좌 상
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def search():
    # x, y, 방향, 누적 회전 수
    x, y, k, cnt = 0, 0, 0, 0
    start = [x, y, k, cnt]
    # 모든 사과에 대해서 순회
    for apple in target_list:
        # 대상 사과
        apple_pos = [apple[1], apple[2]]
        queue = deque()
        # 내 위치, 이동 방향
        queue.append(start)
        while queue:
            x, y, k, cnt = queue.popleft()
            nx, ny = x + dx[k], y + dy[k]
            # 사과 찾았으면 종료.
            if [nx, ny] == apple_pos:
                start = [nx, ny, k, cnt]
                break
            # 범위 벗어나면 무시
            if not (0 <= nx < N and 0 <= ny < N): continue
            # 현재 방향으로 직진
            queue.append((nx, ny, k, cnt))
            # 방향 바꿀거면? 현재 위치에서 방향만 바꾸기
            k = (k+1) % 4
            queue.append((x, y, k, cnt+1))
    return cnt  # 모든 조사가 종료된 시점의 최종 회전수


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    x, y = 0, 0
    target = 1
    target_list = []   # 시작 지점 초기화
    # 전체 순회하여 사과 위치 찾기
    for i in range(N):
        for j in range(N):
            if data[i][j] != 0:
                target_list.append([data[i][j], i, j])
    target_list.sort()  # 사과 번호 순으로 정렬
    print(f'#{tc} {search()}')