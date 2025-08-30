import sys
sys.stdin = open('sample_input.txt', 'r')
import heapq, math

def dijkstra():
    distance = {v: math.inf for v in graph}
    distance[0] = 0
    min_heap = []
    heapq.heappush(min_heap, [0, 0])
    visited = set()

    while min_heap:
        dist, current = heapq.heappop(min_heap)
        if current in visited or distance[current] < dist:
            continue
        visited.add(current)

        for next, w in graph[current]:
            next_dist = dist + w
            if next_dist < distance[next]:
                distance[next] = next_dist
                heapq.heappush(min_heap, [next_dist, next])
    return distance

T = int(input())
for tc in range(1, T+1):
    N, E = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(E)]
    graph = {v: [] for v in range(N+1)}
    for s, e, w in edges:
        graph[s].append((e, w))
    
    result = dijkstra()
    print(result[N])