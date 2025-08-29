import sys
sys.stdin = open('sample_input.txt', 'r')
'''
    - n, a, b가 주어지면 (x+y)^n에서 x^ay^b의 계수를 구하는 로직
'''
T = int(input())
for tc in range(1, T+1):
    n, a, b = map(int, input().split())

    dp = [[0 for _ in range(a+1)] for _ in range(n+1)]
    
    for i in range(n+1):
        for j in range(min(i, a)+1):
            if i == j or j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
    
    print(f'#{tc}', dp[n][a])
