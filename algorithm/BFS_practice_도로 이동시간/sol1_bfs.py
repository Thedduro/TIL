import sys
from collections import deque

sys.stdin = open('input.txt')

# 상 하 좌 우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def BFS(row, col):
    queue = deque()
    queue.append((0,0)) # 시작 정점 후보군에 삽입
    distance[0][0] = 0 # 시작위치 까지 이동거리는 0

    # BFS 탐색
    while queue:
        row, col = queue.popleft()

        for k in range(4): # 4방향 탐색
            nx = row + dx[k]
            ny = col + dy[k]

            # 리스트의 범위를 벗어나지 않는지 확인
            # 이전에 방문한 적이 없어야 함> -1 로 초기화 아니면 방문했다
            # 위치가 길이어야 함 > 1은 길 0은 벽
            if 0 <= nx< N and 0 <= ny < M and distance[nx][ny]== -1 and data[nx][ny]:
                # 위 조건 모두 만족시에만 후보군에 들 수 있음
                queue.append((nx, ny))

                # 다음 위치까지 도달하는 비용 +1
                distance[nx][ny] = distance[row][col] + 1

                # 도착지점 도착 > BFS 특성상 가장 빠른 길 > 그때까지 비용 할당후 종료
                if nx == N-1 and ny == M-1 :  # 도착지임
                    return


N, M = map(int,input().split()) # row:N, col:M
data = [list(map(int, input())) for _ in range(N)]

# 해당 위치까지 도달하는데 걸린 비용이 얼마인지 기록
distance = [[-1] * M for _ in range(N)]

BFS(0,0)
print(distance[N-1][M-1])

# 전체 출력
for dis in distance:
    print(*dis) 