import sys
sys.stdin = open('sample_input.txt', 'r')
import heapq

def prim():
    mst = []
    visited = set()
    start = 0

    min_heap = [(w, start, e) for e, w in adj_list[start]]
    heapq.heapify(min_heap)
    visited.add(start)

    while min_heap:
        w, s, e = heapq.heappop(min_heap)
        if e in visited:
            continue
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

    adj_list = {v: [] for v in range(V+1)}
    for s, e, w in edges:
        adj_list[s].append((e, w))
        adj_list[e].append((s, w))
    
    mst = prim()
    print(f'#{tc}', sum(mst))