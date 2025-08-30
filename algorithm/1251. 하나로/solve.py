import sys
sys.stdin = open('re_sample_input.txt', 'r')

'''
    - 최소 신장 트리 알고리즘을 쓴다.
    > Why? 모든 섬을 이어야 함 > 간선의 정보의 합이 최소가 되어야 함
    > 트리 구조를 가지며, 싸이클이 완성되면 최소 탈락!
    
    - 그러면 어떻게 노드를 잇는 간선 정보(환경부담금)를 얻을까?
    - itertools를 써서 2개의 원소를 가지는 모든 조합을 얻음
    - [섬 1, 섬 2, 가중치] = [s, e, w]
'''

    from itertools import combinations
    import math

    def find(parents, n):
        if parents[n] != n:
            parents[n] = find(parents, parents[n])
        return parents[n]

    def union(parents, x, y):
        root_x = find(parents, x)
        root_y = find(parents, y)

        if root_x < root_y:
            parents[root_y] = root_x
        else:
            parents[root_x] = root_y


    T = int(input())
    for tc in range(1, T+1):
        N = int(input())
        X = list(map(int, input().split()))
        Y = list(map(int, input().split()))
        E = float(input())
        islands = [(i, X[i-1], Y[i-1]) for i in range(1, N+1)] # 섬의 좌표 

        edges = [] # 모든 간선 정보를 담는 리스트
        for island1, island2  in combinations(islands, 2):
            # 해저터널의 길이를 구한다
            L = math.sqrt((island1[1] - island2[1])**2 + (island1[2] - island2[2])**2)
            edges.append((island1[0], island2[0], E*(L**2))) # s, e, w
        edges.sort(key = lambda x: x[2]) # 가중치가 작은 것 부터 정렬 

        parents = [i for i in range(N+1)]
        mst= []
        for edge in edges:
            s, e, w = edge
            if find(parents, s) != find(parents, e): # 둘이 같은 집합이 아니라면 > 같은 집합으로 묶기
                union(parents, s, e)
                mst.append(w) # 가중치를 추가
                if len(mst) >= N-1: # 근데 만약에 간선이 N-1이 넘었다면 종료
                    break
        
        print(f'#{tc}', round(sum(mst)))
