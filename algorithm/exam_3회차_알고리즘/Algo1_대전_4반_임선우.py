'''
    최소 비용의 엣지 구축
    > 최소 신장 트리 문제임.
    + 모든 정거장 연결이 불가능? > -1 출력
    >> kruskal 알고리즘으로 구현한다. 
'''
def find_parent(x):
    if x != parents[x]:
        parents[x] = find_parent(parents[x])
    return parents[x]

def union(x, y):
    root_x = find_parent(x)
    root_y = find_parent(y)

    if root_x < root_y:
        parents[root_x] = root_y
    else:
        parents[root_y] = root_y
        
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(M)]
    edges.sort(key = lambda x: x[2])
    parents = [i for i in range(N+1)]

    # 연결 가능 조건 검사
    for i in range(M-1):
        cur = edges[i]
        s, e, w = cur[0], cur[1], cur[2]
        flag = False
        for j in range(i+1, M):
            next = edges[j]
            lst = [next[0], next[1]]
            if s in lst or e in lst:
                flag = True
    if flag == False: # 모든 노드와 노드의 연결을 확인했는데도 False? > 연결이 끊김.
        print(f'#{tc}', -1)
        continue

    mst = []
    for edge in edges:
        s, e, w = edge[0], edge[1], edge[2]

        if find_parent(s) != find_parent(e):
            union(s, e)
            mst.append(w)

    print(f'#{tc}', sum(mst))