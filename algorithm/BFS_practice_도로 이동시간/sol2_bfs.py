import sys
from collections import deque

sys.stdin = open('input.txt')

# 상 하 좌 우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def BFS(road, N, M):
    # sol1에 단순 좌표만 넣었다면 > 이번엔 후보군에 , 그 후보군이 얼만큼 누적시간을 가지고 있는지도 함께 기록
    queue = deque()
    queue.append((0,0,0)) # x, y, cnt

    visited = [[0] * M for _ in range(N)]
    visited[0][0] = 1 # 시작지점의 방문 처리

    while queue:
        row, col, dist = queue.popleft()

        for k in range(4):
            nx = row + dx[k]
            ny = col + dy[k]

            # 범위를 벗어났으면 조사 못함
            if nx < 0 or nx >= N or ny < 0 or ny >= M: continue

            # 이미 방문한 경우
            if visited[nx][ny]: continue
            
            # 길이 아닌 경우
            if road[nx][ny] == 0: continue
            
            # 도착 지점인 경우 > 도달 시간 반환
            if nx == N-1 and ny == M-1:
                return dist + 1
            
            # 위의 조건을 모두 통과 > 다음 후보군에 등록
            visited[nx][ny] = 1
            queue.append((nx, ny, dist + 1)) 


# 도로의 크기 N * M 입력 받기
N, M = map(int, input().split())
road = [list(map(int, input())) for _ in range(N)]
result = BFS(road, N, M)
print(result)
