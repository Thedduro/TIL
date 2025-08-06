import sys
from collections import deque
sys.stdin = open('input.txt', 'r')

# 상 하 좌 우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def BFS(data, row, col):
    queue = deque()
    queue.append((row,col)) # 시작 지점 넣기

    visited = [[0] * 100 for _ in range(100)] # 방문 처리할 리스트
    visited[row][col] = 1 # 시작지점의 방문 처리

    while queue:
        row, col = queue.popleft()

        for i in range(4): # 상하좌우(자식노드) 탐색
            nx, ny = row + dx[i], col + dy[i] # 다음 탐색 노드
            
            if visited[nx][ny]: # 방문했다면
                continue ## 그냥 단순 도달가능 여부를 물어보는 문제니까 필요 x > 지나온 자리를 1로 표시하면 되지 않을까?
            if nx < 0 or nx >= 100 or ny < 0 or ny >= 100: # 인덱스를 넘었다면 
                continue ## 겉이 다 벽이니까 조건 필요 x
            if data[nx][ny] == 1: # 벽이면
                continue 
            if data[nx][ny] == 3: # 도착지점에 도착하면, 리턴
                return 1
            
            # 위의 조건을 모두 통과 > 다음 후보군에 등록
            visited[nx][ny] = 1
            queue.append((nx,ny))
    
    return 0 # while문을 다 돌았는데도 return을 못했어? > 그럼 도착 할 수 없는 맵이다. > 0 리턴

def find_start(data): # 시작지점 찾기
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == 2:
                return i, j

for _ in range(1, 11):
    tc = int(input())
    data = [list(map(int, input())) for _ in range(100)]
    
    start, end = find_start(data)
                
    print(f'#{tc} {BFS(data, start, end)}')