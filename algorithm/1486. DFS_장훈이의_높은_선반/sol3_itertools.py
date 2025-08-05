import sys
from itertools import combinations

sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T + 1):
    # N: 사람 수, B: 목표 높이
    N, B = map(int, input().split())
    # 각 사람의 키를 입력 받아 리스트로 저장
    arr = list(map(int, input().split()))

    # 직원당 키는 최대 10000이므로, 최대 높이는 10000 * N
    min_height = 10000 * N 

    # 1부터 N개 까지를 선택한 조합
    for r in range(1, N+1):
        for comb in combinations(arr, r):
            total = sum(comb)

            if total >= B:
                min_height = min(min_height, total)


    # 목표 높이 B를 빼서 실제로 초과된 부분만 출력
    print(f"#{tc} {min_height - B}")