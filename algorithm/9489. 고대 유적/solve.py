import sys
sys.stdin = open('input1.txt', 'r')

'''
    - 좌표정보, 방향정보를 함께 저장
    - 처음에는 방향정보가 0 이면 방향탐색 ( 하, 우 로만 움직임 > 중복 탐색 최소화)
    - 아니면, 방향정보로만 움직임 0이면 종료
'''

# def find(x, y, dir, cnt):
#     for d in dir:
#         nx, ny = x + d[0], y + d[1]
#         if nx < 0 or nx >= M or ny < 0 or ny >= N: continue
#         if lagacy[nx][ny] == 1:

#     lagacy[i][j]

def dfs(x, y, dx, dy):
    # (x,y)에서 시작해 (dx,dy) 방향으로 직선 DFS
    if not (0 <= x < N and 0 <= y < M):
        return 0
    if lagacy[x][y] == 0:
        return 0
    # 현재 칸 포함 + 다음 칸 탐색
    return 1 + dfs(x+dx, y+dy, dx, dy)


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    lagacy = [list(map(int, input().split())) for _ in range(N)]

    result = 0

    for i in range(N):
        for j in range(M):
            if lagacy[i][j] == 0: continue

            if j > 0 and lagacy[i][j-1] == 1: continue # 평행라인의 첫번째 x(가로 시작점이 아님)
            if i > 0 and lagacy[i-1][j] == 1: continue # 수직라인의 첫번째 x(세로 시작점이 아님)

            if lagacy[i][j] == 1:
                result = max(result, dfs(i, j, 0, 1)) # 오른쪽 탐색
                result = max(result, dfs(i, j, 1, 0)) # 아래쪽 탐색

    print(f'#{tc}', result)
    