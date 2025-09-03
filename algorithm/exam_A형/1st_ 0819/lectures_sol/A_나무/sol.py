import sys
sys.stdin = open('input.txt')


def is_possible(x, diffs):
    # x일 동안 줄 수 있는 물의 총 양 계산
    ones = (x + 1) // 2     # 홀수 날: +1씩
    twos = x // 2           # 짝수 날: +2씩

    # 물주기로 키워야 하는 전체 합
    total_diff = sum(diffs)
    # 전체 물 주기 합이 부족하면 당연히 불가능
    if ones + 2 * twos < total_diff:
        return False

    # 각 나무마다 필요한 물의 양 diff를
    # 1과 2의 조합으로 나타낼 때,
    odd = 0   # 각 나무에서 무조건 필요한 홀수 날의 횟수 (diff가 홀수면 최소 1)
    even = 0       # 나머지 2씩 채워야 하는 횟수 (물주기를 2씩 묶어 표현)
    for d in diffs:
        if d % 2 == 1:
            odd += 1
            even += (d - 1) // 2
        else:
            even += d // 2

    # 최소 하루씩 줘야 하는 물 수보다
    # 내가 줄 수 있는 하루치씩의 물 양이 더 적으면 성장 불가
    if ones < odd:
        return False
    # 나머지 (ones - odd)개의 홀수 날은 1+1로 2를 만드는 역할을 할 수 있음.
    # 따라서 짝수 날 twos와 (ones - odd)//2 쌍을 합쳐 even을 채울 수 있어야 함.
    if twos + (ones - odd) // 2 < even:
        return False

    return True


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = list(map(int, input().split()))
    M = max(data)   # 최대 높이 나무
    # 각 나무마다 추가로 필요한 높이 차이
    diffs = [M - h for h in data]

    # 만약 이미 모두 최대 높이라면 0일
    if sum(diffs) == 0:
        print(f'#{tc} 0')
        continue

    # 이진 탐색: 충분한 일수 x의 최솟값을 찾는다.
    lo, hi = 1, 100000  # 충분히 큰 상한
    while lo < hi:
        mid = (lo + hi) // 2            # 중앙 값을 찾고,
        if is_possible(mid, diffs):     # 나무를 키울 수 있는 최소한도를 찾으면
            hi = mid                    # 최댓값을 갱신
        else:
            lo = mid + 1                # 못찾은 경우, 1일차부터 다시 계산
    print(f'#{tc} {lo}')

