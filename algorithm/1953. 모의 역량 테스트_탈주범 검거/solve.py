import sys
from collections import deque

sys.stdin = open("sample_input.txt", "r")

# 방향 벡터: 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 각 파이프 번호별로 이동 가능한 방향
# 숫자는 dx/dy 인덱스에 대응됨 (0: 상, 1: 하, 2: 좌, 3: 우)
pipe_type =  {
    1: [0, 1, 2, 3],       # 상, 하, 좌, 우
    2: [0, 1],             # 상, 하
    3: [2, 3],             # 좌, 우
    4: [0, 3],             # 상, 우
    5: [1, 3],             # 하, 우
    6: [1, 2],             # 하, 좌
    7: [0, 2],             # 상, 좌
}

# 현재 노드와 다음 노드의 연결 확인
def check_pass(dir, nx, ny):
    """
    dir: 현재 위치에서 이동한 방향
    nx, ny: 이동하려는 위치 좌표
    """
    # dir이 상(0) 또는 좌(2)일 때, 그 반대인 하(1) 또는 우(3)가 다음 위치 파이프에 있어야 연결 가능
    if dir == 0 or dir == 2: 
        if dir + 1 in pipe_type[data[nx][ny]]: # 자식과 부모가 이어져 있으면
            return True
    # dir이 하(1) 또는 우(3)일 때, 그 반대인 상(0) 또는 좌(2)가 다음 위치 파이프에 있어야 연결 가능
    if dir == 1 or dir == 3:
        if dir - 1 in pipe_type[data[nx][ny]]:
            return True
        
    return False # 부모와 자식이 이어져있지 않을때


def BFS(data, row, col, L):
    cnt = 1 # 시작 위치도 1시간 소요됨

    visited = [[False]*M for _ in range(N)] # 방문 여부 저장

    queue = deque()
    queue.append((row, col, cnt)) # 시작지점, 반복횟수 추가
    visited[row][col] = True
    
    possible_position = set() # 가능한 위치 수집
    possible_position.add((row,col))

    while queue: # 시간 제한 도달 시 탐색 종료
        row, col, cnt = queue.popleft()

        if cnt == L: 
            return possible_position

        # 현재 파이프 종류로 갈수 있는 방향 탐색
        for dir in pipe_type[data[row][col]]: 
            nx, ny = row + dx[dir], col + dy[dir]

            if nx < 0 or nx >= N or ny < 0 or ny >= M: # 인덱스를 넘었다면
                continue
            
            if data[nx][ny] == 0: # 파이프가 없다면
                continue

            if visited[nx][ny]: # 이미 방문을 했다면 해당 위치를 추가할 필요 없음
                continue

            # 파이프가 연결되있음을 어떻게 알지?
            if check_pass(dir, nx, ny):
                queue.append((nx,ny, cnt+1)) # 다음 위치와 시간+1 저장
                visited[nx][ny] = True
                possible_position.add((nx,ny)) # 가능한 위치로 추가

    return possible_position

T = int(input())

for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]


    print(f'#{tc} {len(BFS(data, R, C, L))}')
