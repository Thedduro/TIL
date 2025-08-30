import sys
sys.stdin = open('sample_input.txt', 'r')
import heapq, math

def bellman_ford():
    distance = {v: math.inf for v in graph}
    distance[0] = 0

    for _ in range(N-1):
        flag = False
        for v in graph:
            for next, w in graph[v]:
                if distance[v] != math.inf and distance[v] + w < distance[next]:
                     distance[next] = distance[v] + w
                     flag = True
        if flag == False:
            break

    # 음수 사이클 검사 > 하지만, 이 문제는 음수 가중치가 없으므로 해당 없음
    # 벨만포드 알고리즘에서는 음수사이클 겁사가 필요함
    for v in graph:
        for next, w in graph[v]:
            # 다 돌았는데, 또 갱신해야 하는 상황 발생? > 이거 음수 사이클이 있구나
            if distance[v] != math.inf and distance[v] + w < distance[next]:
                return False
    return distance


T = int(input())
for tc in range(1, T+1):
    N, E = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(E)]
    graph = {v: [] for v in range(N+1)}
    for s, e, w in edges:
        graph[s].append((e, w))

    print(bellman_ford())