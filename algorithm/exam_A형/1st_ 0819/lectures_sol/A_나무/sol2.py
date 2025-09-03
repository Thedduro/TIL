import sys
sys.stdin = open('input.txt')

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

    # 각 나무가 홀수 날의 +1을 꼭 받아야 하는 경우의 수
    odd = sum(1 for d in diffs if d % 2 == 1)
    x = odd  # 최소 x일은 홀수 물주기 횟수를 만족해야 하므로

    while True:
        ones = (x + 1) // 2     # x일 중 홀수 날 수
        twos = x // 2           # x일 중 짝수 날 수

        if ones < odd:
            x += 1
            continue

        # 각 나무에 대해, d가 홀수면 1은 반드시 홀수 날로 채워야 하고 나머지 (d-1)은 2씩 채울 수 있음.
        # d가 짝수면 d 전체를 2씩 채울 수 있다.
        even = sum(d // 2 for d in diffs)
        # 추가로 홀수 날 중 odd_required를 제외한 날은 1+1 = 2로 사용 가능.
        if twos + (ones - odd) // 2 >= even:
            print(f"#{tc} {x}")
            break
        x += 1