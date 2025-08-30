import sys
sys.stdin = open('s_input.txt', 'r')

def find_parent(x):
    if parents[x] == x:
        return parents[x]
    return find_parent(parents[x])

def union(x, y):
    root_x = find_parent(x)
    root_y = find_parent(y)

    if root_x != root_y:
        if rank[root_x] < rank[root_y]:
            parents[root_x] = root_y
        elif rank[root_x] > rank[root_y]:
            parents[root_y] = root_x
        else:
            parents[root_y] = root_x
            rank[root_x] += 1

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(M)]
    parents = [i for i in range(N+1)]
    rank = [0] * (N+1)

    for a in arr:
        union(a[0], a[1])
    
    result = set(find_parent(p) for p in parents[1:])
    print(f'#{tc}', len(result))