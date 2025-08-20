import sys
sys.stdin = open('sample_input.txt', 'r')

'''
    - 1 > 집합에 포함되어 있는지 확인
    - 0 > 합집합 연산을 실행
'''

def find_parent(parents, x):
    if parents[x] != x:
        parents[x] = find_parent(parents, parents[x])
    return parents[x]

def union(parents, x, y):
    root_x = find_parent(parents, parents[x])
    root_y = find_parent(parents, parents[y])

    if root_x < root_y:
        parents[root_y] = root_x
    else:
        parents[root_x] = root_y

T = int(input())
for tc in range(1, T+1):
    N, M =  map(int, input().split())
    items = [list(map(int, input().split())) for _ in range(M)]
    parents = [i for i in range(N+1)]

    result = ''

    for item in items:
        x, y = item[1], item[2]
        if item[0] == 1:
            if find_parent(parents, x) == find_parent(parents, y): # 같은 집합에 포함(최상단 노드가 같으면)
                result += '1'
            else:
                result += '0'
        else:
            union(parents, x, y)

    print(f'#{tc}', result)