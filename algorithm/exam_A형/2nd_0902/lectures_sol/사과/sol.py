import sys
sys.stdin = open('input.txt')

from collections import deque

# 우회전만 가능?
# 우 하 좌 상
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def search():
    global target_cnt, result
    queue = deque()
    # 좌표, 대상, 방향, 누적 회전 횟수
    # queue.append((x, y, target, k, acc))
    queue.append((0, 0, 1, 0, 0))
    all_of_target_num = 1           # 모두가 공유하는 현재 타겟
    while queue:
        x, y, target, k, acc = queue.popleft()
        nx, ny = x + dx[k], y + dy[k]
        # print(nx, ny, k)
        # 이미 충분히 회전했으면 무시
        if acc >= result: continue
        # 이전에 누군가가 내 타겟을 먹었으면 무시
        if target < all_of_target_num: continue
        # 범위 안이면 일단 이동
        if 0 <= nx < N and 0 <= ny < N:
            if data[nx][ny] == target:  # 먹어야 할 사과면
                target += 1             # 다음 대상
                all_of_target_num += 1

                if target == target_cnt+1:    # 다 먹었으면
                    result = min(result, acc)   # 최소 회전 횟수 초기화
            # 먹을 사과든 아니든 가던 방향으로 전진
            queue.append((nx, ny, target, k, acc))
            k = (k + 1) % 4 # 방향 전환 해서 전진
            queue.append((nx, ny, target, k, acc+1))
        # 범위를 벗어날 것 같으면 현재 위치에서 회전만
        else:
            k = (k + 1) % 4  # 방향 전환 해서 전진
            queue.append((x, y, target, k, acc + 1))

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    x, y = 0, 0
    target = 1
    target_cnt = 0
    result = float('inf')
    # 전체 순회하여 사과 총 개수 누적
    for i in range(N):
        for j in range(N):
            if data[i][j] != 0:
                target_cnt += 1
    search()
    print(f'#{tc} {result}')