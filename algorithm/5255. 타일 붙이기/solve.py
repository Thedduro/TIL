import sys
sys.stdin = open('sample_input.txt', 'r')

'''
    DP알고리즘: 바텀업(상향식)방법으로 간다.
    N = 1 > 1
    N = 2 > 3
    N = 3 > 6
    N = 4 > n-1 + n-2*2 + n-3
'''

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    dp = [0] * (N+1)

    dp[1], dp[2], dp[3] = 1, 3, 6

    for n in range(4, N+1):
        dp[n] = dp[n-1] + dp[n-2]*2 + dp[n-3] # 타일 붙이기의 점화식
    
    print(f'#{tc}', dp[N])
    