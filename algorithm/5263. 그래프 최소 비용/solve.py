import sys
sys.stdin = open('sample_input.txt', 'r')

'''
    플로이드-워셜 알고리즘을 사용하여 음수도 고려가 가능하게끔 한다.
    - 모든 정점 쌍 간의 최단 경로를 구해야 한다. 
    최단 경로들을 저장하여, 이 중에 가장 최대인 값을 출력
'''
# graph = {idx+1: {} for idx in range(N)} # 그래프 구현(인접 리스트) {1: {2: 27, 3: 44}, 2: {1: -5, 3: 62}, 3: {1: 0, 2: 99}}
#     for i in range(N):
#         for j in range(N):
#             if i != j:
#                 graph[i+1][j+1] = lst[i][j]
#     result = find(graph, 1)

T = int(input())
for tc in range(1, T+1):
    N = int(input()) # 노드의 개수
    graph = []
    for i in range(N):
        row = list(map(int, input().split()))
        for j in range(N):
            if i != j and row[j] == 0:
                row[j] = float('inf')
        graph.append(row)

    for k in range(N):
        for i in range(N):
            for j in range(N):
                Dik = graph[i][k]
                Dkj = graph[k][j]
                Dij = graph[i][j]

                if Dik + Dkj < Dij:
                    graph[i][j] = Dik + Dkj

    max_value = 0
    for i in range(N):
        for j in range(N):
            if i != j:
                if graph[i][j] > max_value:
                    max_value = graph[i][j]
    print(f'#{tc}', max_value)
