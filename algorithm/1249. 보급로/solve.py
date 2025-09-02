import sys
sys.stdin = open('input.txt', 'r')

'''
    도로 손상에 비례해 복구 시간 증가
    현재 칸 도로 복구를 모두 해야지 다음 칸 이동 가능
    출발 > 도착까지 복구시간이 가장 짧은 총 복구시간
    - 다익스트라 알고리즘으로 최단경로를 구하면 될듯?
        > 도로의 손상 정도가 곧 가중치가 됨. 
'''

import heapq, math
direction = [(-1,0),(1,0),(0,-1),(0,1)]

def find():
    INF = math.inf
    distance = [[INF for _ in range(N)] for _ in range(N)]

    heap = []
    heapq.heappush(heap, (0,0,0))
    distance[0][0] = 0

    while heap:
        w, x, y = heapq.heappop(heap)
        
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            else:
                next_w = load[nx][ny] + w
                if next_w < distance[nx][ny]: # 갱신
                    distance[nx][ny] = next_w
                    heapq.heappush(heap, (next_w, nx, ny))

    return distance[N-1][N-1]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    load = [list(map(int, input())) for _ in range(N)]

    print(f'#{tc}', find())
