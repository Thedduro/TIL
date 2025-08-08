import sys
sys.stdin = open("input.txt", "r")

# 아래 방향으로 진행하면서 좌우 방향으로 이동 가능한 통로가 나타나면 방향 전환을 하게 된다.

direction = [ (0,-1), (0,1), (-1,0)] 

def dfs(i, j, visited):
    current_value = ladder[i][j] # 현재의 값

    # BASE_CASE
    if current_value == 1 and i == 0:
        return j
    
    visited[i][j] = True # 방문 처리
    
    for dx , dy in direction: # 좌 우 하 순으로 순회
        nx, ny = i + dx, j+ dy # 다음 방향

        if nx < 0 or nx >= 100 or ny < 0 or ny >= 100: # 범위 벗어나면
            continue

        if ladder[nx][ny] == 0: # 길이 아니면
            continue

        if not visited[nx][ny]: # 방문 안했으면
             result = dfs(nx, ny, visited)
             if result is not None:
                 return result

for _ in range(1, 11): # 10개의 테스트케이스가 주어짐
    tc = int(input()) # 테스트 케이스 번호
    ladder = [list(map(int, input().split())) for _ in range(100)] # 사다리의 2차원 행렬


    # 도착지점 찾기
    for idx in range(100):
        if ladder[-1][idx] == 2:
            end_idx = idx

    visited = [[False] * 100 for _ in range(100)] 

    print(f'#{tc} {dfs(99, end_idx, visited)}')