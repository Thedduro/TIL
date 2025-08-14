import sys
sys.stdin = open("input.txt", "r")

# 도착 지점에서 좌, 우 경로가 있다면 거기로 간ㅁ 없다면 위로 감
# 계속 가다가 1을 만나면 그 위치의 x좌표를 반환함
# 종료 조건? x좌표가 0, 정답일때
# visited 를 쓰는 이유 > 좌로 이동했다가 반복문에서 다음 우로 이동 > 제자리 돌아

direction = [(0,-1),(0,1),(-1,0)]

def find_end():
    for j in range(100):
        end_idx = ladder[99][j]
        if end_idx == 2:
           return j

def dfs(x, y):
    if x == 0 and ladder[x][y] == 1:
        return y
    
    for dir in direction:
        nx, ny = x + dir[0], y + dir[1]

        if 0<=nx<100 and 0<=ny<100 and ladder[nx][ny] == 1:
            if not visited[nx][ny]:
                visited[nx][ny] = True
                result =  dfs(nx,ny)
                if result is not None:
                    return result

for _ in range(1, 11): # 10개의 테스트케이스가 주어짐
    tc = int(input()) # 테스트 케이스 번호
    ladder = [list(map(int, input().split())) for _ in range(100)] # 사다리의 2차원 행렬
    
    end_idx = find_end() # 도착지점의 위치 찾기
    visited = [[False]*100 for _ in range(100)]


    print(dfs(99, end_idx))