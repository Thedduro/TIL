import sys
sys.stdin = open("input.txt", "r")

direction = [(1,0), (0,-1), (0,1)] # 하 좌 우

def dfs(i, j):  
    current_value = ladder[i][j] # 현재의 값
    
    # BASE_CASE
    if current_value == 2 and i == 99:
        return True
    
    visited[i][j] = True # 방문 처리 함
    
    for dx , dy in direction:
        nx, ny = i + dx, j+ dy

        if nx < 0 or nx >= 100 or ny < 0 or ny >= 100: # 범위 벗어나면
            continue

        if ladder[nx][ny] == 0: # 길이 아니면
            continue

        if not visited[nx][ny]:
             dfs(nx, ny)
             visited[nx][ny] = False


for _ in range(1, 11): # 10개의 테스트케이스가 주어짐
    tc = int(input()) # 테스트 케이스 번호
    ladder = [list(map(int, input().split())) for _ in range(100)] # 사다리의 2차원 행렬
    
    # 방문 배열 및 최소 이동 횟수 초기화
    visited = [[False] * 100]   

    # 출발지점 찾기
    start_idx = []
    for idx in range(100):
        if ladder[0][idx] == 1:
            start_idx.append(idx)

    # 각 출발지점을 순회하며 정답일때 저장
    def find():
        for s in start_idx: 
            if dfs(0, s):
                return s
            
    print(f'#{tc} {find()}')
