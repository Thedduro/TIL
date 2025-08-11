
def comb(M, K):
    visited = [False] * N_ingre

    if K < 0: # BASE 케이스
        return 
    if K == 0:
        return  
    for i in range(N_ingre):
        for m in range(M):
            if not visited[i]:
                visited[i] = True
                K = ingre[i]
                visited[i] = False
            

def solve(ingre):
    M, K, L = ingre[0], ingre[1], ingre[2]

    sum = 0
    
    result = []

    for _ in range(M):
        comb(ingre, M, K, result)

    if sum == L: # 생성가능 하면 바로 리턴
        return L
    

T = int(input()) 

for tc in range(1, T+1):
    N = int(input())

    ingre = [list(map(int, input().split())) for _ in range(N)]

    N_ingre  = int(input())
    data = list(map(int, input().split()))
    
    result = []
    for i in range(N):
        result.append(solve(ingre[i]))

    print(f'#{tc}', N, ingre, N_ingre, data)