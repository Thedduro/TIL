import sys
sys.stdin = open("sample_input.txt", "r")

def find(start, total_value, cnt): # 백트래킹을 활용한 DFS 구현 
    global min_value

    if cnt == N:
        if operation[start][0] != 0:  # 시작점(0)으로 돌아가는 경로가 존재할 경우
            result = total_value + operation[start][0] # 총 비용 계산
            min_value = min(min_value, result) # 최소 비용을 갱신

    if total_value >= min_value: # promissing이 아닌것 같으면? 부모 노드로 돌아감
        return # 현재까지의 비용이 이미 구한 최소값보다 크거나 같으면 더 탐색할 필요 없음 (가지치기)
    
    for child in range(N):
        if not visited[child] and operation[start][child] != 0: # 방문하지 않았고 경로가 존재할 경우
            current_value = operation[start][child] # 이동 비용 저장

            visited[child] = True # 방문 처리
            find(child, total_value + current_value, cnt+1)
            visited[child] = False # 백 트래킹

T = int(input())

for tc in range(1, T+1):
    N = int(input()) # 수행해야하는 연산 횟수
    operation = [list(map(int, input().split())) for _ in range(N)] # 연산 정보

    visited = [False] * N
    visited[0] = True
    INF = float('inf')
    min_value = INF
    find(0, 0, 1)

    print(f'#{tc} {min_value}')