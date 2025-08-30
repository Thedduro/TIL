import sys
sys.stdin = open('sample_input.txt', 'r')

def find_parent(x):
    if parent[x] == x:
        return x
    return find_parent(parent[x])

def union(x, y):
    root_x = find_parent(x)
    root_y = find_parent(y)

    if root_x != root_y:
        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        elif rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        else:
            parent[root_y] = root_x
            rank[root_x] += 1

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(E)]
    edges.sort(key = lambda x: x[2])

    parent = [i for i in range(V+1)]
    rank = [0] * (V+1)

    mst = []
    for x, y, w in edges:
        if find_parent(x) != find_parent(y):
            union(x, y)
            mst.append(w)
        if len(mst) > V-1:
            break

    print(f'#{tc}', sum(mst))