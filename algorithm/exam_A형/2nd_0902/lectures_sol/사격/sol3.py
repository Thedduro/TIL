import sys
sys.stdin = open('input.txt')

def search(mask):
    # 모든 풍선을 다 터뜨다.
    # 더 이상 터트릴 풍선이 없다 -> 더해질 점수가 0점
    if mask == 0:
        return 0

    # 현재 상태(mask상태가 0100 이면 8번째 경우의 수)에 대한 최대 점수가 이미 계산되었다면,
    # 다시 계산할 이유 없음
    if memo[mask] != -1:
        return memo[mask]

    max_val = 0
    # 각 풍선에 대해서
    for i in range(N):
        # 이번 경우에 i번째 풍선 터트릴지 고민
        if (mask >> i) & 1:
            # 1. i번쨰를 터트를 꺼라면, 왼쪽 오른쪽 찾아야함
                # 왼쪽 끝까지 탐색해도 없으면 -1로 초기화
            left, right = -1, -1
            # 왼쪽 찾기 \ (for가 생각하기 쉬울 듯)
            for l in range(i - 1, -1, -1):
                # 마찬가지로 이번 경우에서 l번째 풍선 살아있으면
                if (mask >> l) & 1:
                    left = data[l]  # 왼쪽 점수
                    break
            # 오른쪽 동일
            for r in range(i + 1, N):
                if (mask >> r) & 1:
                    right = data[r]
                    break
            # 점수 계산
            score = 0
            # 양쪽 다 못 찾았으면 그냥 내 점수만
            if left == -1 and right == -1:
                score = data[i]
            elif left == -1:     # 왼쪽만 못 찾았으면
                score = right    # 오른쪽만
            elif right == -1:
                score = left
            else:                # 둘다 찾았으면 곱하기
                score = left * right

            # 3. 현재 점수 + i번째 풍선 터트렸을 때 얻을 수 있는 최고 점수 계산
                # i 번째 풍선 터트려야 겠네?
                # mask XOR (1 << i)
                '''
                    a = 7   (111)
                    b = 1   (001)
                    a ^ b   (110)

                    a = 7   (111)
                    c = 2   (010)
                    a ^ c   (101)
                '''
            val = score + search(mask ^ (1 << i))
            max_val = max(max_val, val)

    # 4. 이번 회차 최대 점수 메모
    memo[mask] = max_val
    return max_val


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    data = list(map(int, input().split()))

    # 메모이제이션 -1(아직 계산 안 됨)로 초기화
    # 모든 경우의 수 2^N개
    # 1 1 1 1 <- 모든 풍선이 살아 있는 상태 (1<<N) -1
    # 1 1 1 0 <- 4번째 풍선만 터트린 경우
    # 1 0 1 0 <- 2번째, 4번째 풍선을 터트린 경우
    # 0 0 0 0 <- 모든 풍선을 터트린 경우
    memo = [-1] * (1 << N)

    # (1 << N) - 1은 모든 비트가 1인 상태,
    # 즉 모든 풍선이 살아있는 초기 상태
    result = search((1 << N) - 1)
    print(f'#{tc} {result}')