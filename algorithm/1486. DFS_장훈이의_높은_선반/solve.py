import sys
sys.stdin = open('input.txt', 'r')

'''
    - 자료구조에 직원의 키를 넣음 > sum : 해당 탑의 높이
    - 완성된 탑 중에 B보다 크면서도 그 중 가장 작은 것
    
    - DFS 구현:
        - 직원이 1명일때, 2명일때....
        - 직원이 N보다 커지면 종료
        - 그래서 리스트를 반환

'''
def dfs(n, total):
    global min_result

    if total > min_result: # BASE_CASE 종료 케이스
        return 
    
    if n == N: # 다 탐색했을 경우?
        if total >= B:
            min_result = min(total, min_result)
        return 
    
    dfs(n+1, total + height[n])
    dfs(n+1, total)


T = int(input())

for tc in range(1, T+1):
    N, B = map(int, input().split())
    height = list(map(int, input().split()))

    min_result = 10000*N

    dfs(0,0)
    print(f'#{tc}', min_result-B)