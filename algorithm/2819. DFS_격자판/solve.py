import sys
sys.stdin = open('sample_input.txt')

direction = [(-1, 0),(1, 0),(0, -1), (0, 1)] # 상하좌우 방향

def dfs(x, y, current_num):
    global result, direction

    if len(current_num) == 7: # 현재까지 저장된 숫자 길이가 7인 경우
        result.add(current_num)
        return 

    for (dx, dy) in direction:
        nx, ny = x + dx, y + dy

        if 0 <= nx < 4 and 0 <= ny < 4: # 격자판 내에 존재하는지 확인
            dfs(nx, ny, current_num + str(grid[nx][ny])) # current_num: 11이면 문자열 더하기 > 1121 

T = int(input())

for tc in range(1, T+1):
    grid = [list(map(int, input().strip().split())) for _ in range(4)] # 4*4 격자판 생성

    # 저장된 숫자를 담을 인지 > 중복이 되면 안되기 때문에 set 
    result = set()

    for i in range(4):
        for j in range(4):
            dfs(i, j, str(grid[i][j])) # 시작 지점을 모르기 때문에 완전탐색


    print(f'#{tc} {len(result)}')