import sys
sys.stdin = open('s_input.txt', 'r')

def find_p(parent, x):
    if parent[x] != x:
        parent[x] = find_p(parent, parent[x]) # 최상단 루트로 업뎃 해준다
    return parent[x]

def union(parnet, x, y):
    root_x = find_p(parnet, x)
    root_y = find_p(parnet, y)
    if root_x < root_y:
        parent[root_y] = root_x
    else:
        parent[root_x] = root_y

T = int(input())

for tc in range(1, T+1):
    N, M =  map(int, input().split())

    friends = [list(map(int, input().split())) for _ in range(M)]

    parent = [i for i in range(N+1)]

    for friend in friends:
        union(parent, friend[0], friend[1])
    
    result = set(find_p(parent, i)for i in range(1, N+1))

    print(f'#{tc}', len(result))