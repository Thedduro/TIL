import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) # 박스 크기, 상품 개수
    goods = [list(map(int, input().split())) for _ in range(M)]  # 크기, 가격
    # DP[i][j] = i번째 상품까지 고려했을 때, 용량 j에서의 최대 가격
    dp = [[0 for _ in range(N+1)] for _ in range(M+1)]
    
    for i in range(1, M+1): # i는 상품
        size, price = goods[i-1]
        for j in range(N+1): # j는 박스 용량
            if j < size: # 현재 선택한 박스 용량이 size보다 작으면 담을 수 없음
                dp[i][j] = dp[i-1][j]
            else: # 담을 수 있는 경우
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-size] + price)
    print(f'#{tc}', dp[M][N])