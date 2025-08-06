import sys
from collections import deque

sys.stdin = open('input.txt')

# 상 하 좌 우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def DFS(row, col, acc):
    global min_count

    if row == N-1 and col == M-1: # 도착지다
        min_count = min(min_count, acc) # 도착지 까지 도달하는데 걸린 최소 시간 
        return
    
    for k in range(4):
        nx = row + dx[k]
        ny = col + dy[k]

         # 범위를 벗어났으면 조사 못함
        if nx < 0 or nx >= N or ny < 0 or ny >= M: continue

        # 이미 방문한 경우
        if visited[nx][ny]: continue
        
        # 길이 아닌 경우
        if not road[nx][ny]: continue
        
        # 갈 수 있으면 > 방문표시 후 이동
        visited[nx][ny] = 1
        DFS(nx, ny, acc + 1)

        # 조사 갔다 돌아왔다가 다음 조사 후보군 또 조사 > 저번에 조사했던 nx, ny 시점은 없던 일로 해야함.
        visited[nx][ny] = 0
        


# 입력 처리
N, M = map(int, input().split())
road = [list(map(int, input())) for _ in range(N)]

# 방문 배열 및 최소 이동 횟수 초기화
visited = [[False] * M for _ in range(N)]
min_count = float('inf') # 충분히 큰값과 비교하면서 가기 위해

# 시작점 방문처리 후 탐색 시작
visited[0][0] = True
dfs(0, 0, 0)

print(min_count)  # 결과 출력
