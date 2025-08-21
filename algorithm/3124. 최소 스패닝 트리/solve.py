import sys
sys.stdin = open('sample_input.txt', 'r')
import heapq
'''
    - 우선 최소 신장트리를 구현한 후 가중치의 합을 구한다
    - prim 알고리즘을 이용한다
'''

def prim(edges):
    mst = []
    visited = set()
    start_vertex = 1

    min_heap = [(w, start_vertex, e) for e, w in adj_list[start_vertex]]
    heapq.heapify(min_heap)
    visited.add(start_vertex)

    while min_heap:
        w, s, e = heapq.heappop(min_heap)

        if e in visited:
            continue
        # 방문한적이 없으면??
        visited.add(e)
        mst.append(w)

        for next, w in adj_list[e]:
            if next in visited:
                continue
            heapq.heappush(min_heap, (w, e, next))

    return mst


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(E)]
    adj_list = {v: [] for v in range(1, V+1)} # 정점의 인접 리스트
    for s, e, w in edges:
        adj_list[s].append((e, w))
        adj_list[e].append((s, w))

    mst = prim(edges)

    print(f'#{tc}', sum(mst))