import sys
sys.stdin = open('input.txt')

def min_score(n, m, k):
    w = n - m   # 틀린 문제 수
    R = w + 1   # 나눌 공간 수
    safe = R * (k - 1)  # 배수 조건 상관없이 풀 수 있는 문제 수
    # 2배가 전혀 안 생김
    if m <= safe:
        return m

    E = m - safe  # 배수가 무조건 필요한 경우
    D = (E + k - 1) // k  # ceil(E/k)
    L_long = (k - 1) + E
    r = L_long - D * k  # L_long % k

    # 긴 런에서의 점수 + (나머지 런들의 안전 정답)
    return 2 * k * ((1 << D) - 1) + r + (R - 1) * (k - 1)


T= int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    print(f"#{tc} {min_score(N, M, K)}")
