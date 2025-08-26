import sys
sys.stdin = open('sample_input.txt', 'r')
'''
    제약사항 간선의 weight은 모두 양수 > 다익스트라 알고리즘 사용
    - 다익스트라는 우선순위 큐를 사용 > 이걸 통해 최단거리(노드를 거쳐가지 않는) 경로를 선택해 나가면서 갱신한다 
    0 노드 부터 끝 노드 N번 노드까지 걸리는 최소 경로
'''
import heapq
INF = float('inf')

def dijkstra(graph, start):
    distances = {v: INF for v in graph}
    distances[start] = 0

    heap = []
    heapq.heappush(heap, [0, start]) # [도달한거리, 시작정점]
    visited = set()

    while heap:
        dist, current = heapq.heappop(heap)
         # 기존 거리보다, 현재의 거리가 더 크면
        if current in visited or distances[current] < dist: continue
        visited.add(current)

        for next, weight in graph[current].items():
            next_dist = dist + weight
            if next_dist < distances[next]:
                distances[next] = next_dist
                heapq.heappush(heap, [next_dist, next])

    return distances

T = int(input())
for tc in range(1, T+1):
    N, E = map(int, input().split())
    graph = {v:{} for v in range(N+1)}
    for _ in range(E):
        s, e, w = map(int, input().split())
        graph[s][e] = w
    print(f'#{tc}', dijkstra(graph, 0)[N])