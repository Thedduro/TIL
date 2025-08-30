import sys
sys.stdin = open('sample_input.txt', 'r')

def find_parent(parents, x):
    if parents[x] != x:
        parents[x] = find_parent(parents, parents[x])
    return parents[x]

def union(parents, x, y):
    root_x = parents[x]
    root_y = parents[y]

    if root_x < root_y:
        parents[root_y] = root_x
    else:
        parents[root_x] = root_y

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(E)]
    edges.sort(key = lambda x: x[2])
    parents = [i for i in range(V+1)]

    mst =[]
    for edge in edges:
        s, e, w = edge
        if find_parent(parents, s) != find_parent(parents, e):
            union(parents, s, e)
            mst.append(w)
            
    print(f'#{tc}', sum(mst))
